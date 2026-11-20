import pathlib
import re
import urllib.parse
import urllib.request
import json
import yaml

DEVICES_DIR = pathlib.Path("src/devices")
IMAGES_DIR = pathlib.Path("src/images")
USER_AGENT = "ModdableDevicesBot/1.0 (https://github.com/your-username/your-repo)"

def slugify(text: str) -> str:
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug

def search_transparent_image(device_name: str) -> str | None:
    """Queries Wikimedia Commons for a transparent PNG or SVG matching the device."""
    # Bias toward transparent PNGs/SVGs first, then fall back to general PNGs
    queries = [
        f'"{device_name}" filetype:bitmap png',
        f'"{device_name}" filetype:drawing svg',
        f'{device_name} png',
    ]

    for query in queries:
        params = urllib.parse.urlencode({
            "action": "query",
            "format": "json",
            "generator": "search",
            "gsrsearch": f"filetype:png|svg {query}",
            "gsrnamespace": "6",  # File namespace on Wikimedia Commons
            "gsrlimit": "5",
            "prop": "imageinfo",
            "iiprop": "url|mime",
        })
        url = f"https://commons.wikimedia.org/w/api.php?{params}"
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})

        try:
            with urllib.request.urlopen(req, timeout=10) as resp:
                data = json.loads(resp.read().decode("utf-8"))
        except Exception as e:
            print(f"  [!] Search error for '{device_name}': {e}")
            continue

        pages = data.get("query", {}).get("pages", {})
        if not pages:
            continue

        # Sort by search index so the top match is checked first
        sorted_pages = sorted(pages.values(), key=lambda p: p.get("index", 999))
        for page in sorted_pages:
            info = (page.get("imageinfo") or [{}])[0]
            img_url = info.get("url", "")
            mime = info.get("mime", "")
            # Prefer transparent-capable formats (PNG or SVG)
            if img_url and mime in ("image/png", "image/svg+xml"):
                return img_url

    return None

def download_image(url: str, dest_without_ext: pathlib.Path) -> pathlib.Path | None:
    ext = ".svg" if url.lower().endswith(".svg") else ".png"
    dest_path = dest_without_ext.with_suffix(ext)

    req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
    try:
        with urllib.request.urlopen(req, timeout=15) as resp:
            dest_path.write_bytes(resp.read())
        return dest_path
    except Exception as e:
        print(f"  [!] Failed to download {url}: {e}")
        return None

def update_yaml_image_field(yml_path: pathlib.Path, image_rel_path: str):
    """Safely updates or inserts the image: field while preserving comments."""
    lines = yml_path.read_text(encoding="utf-8").splitlines()
    updated = False
    new_lines = []

    for line in lines:
        if re.match(r"^\s*image\s*:", line, re.IGNORECASE):
            new_lines.append(f"image: {image_rel_path}")
            updated = True
        else:
            new_lines.append(line)

    if not updated:
        # Insert right above notes: if present, otherwise append to end
        inserted = False
        final_lines = []
        for line in new_lines:
            if not inserted and re.match(r"^\s*notes\s*:", line, re.IGNORECASE):
                final_lines.append(f"image: {image_rel_path}")
                inserted = True
            final_lines.append(line)
        if not inserted:
            final_lines.append(f"image: {image_rel_path}")
        new_lines = final_lines

    yml_path.write_text("\n".join(new_lines) + "\n", encoding="utf-8")

def main():
    if not DEVICES_DIR.exists():
        print("No src/devices directory found.")
        return

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    added_count = 0

    for yml_file in sorted(DEVICES_DIR.rglob("*.yml")):
        if yml_file.name.startswith("_"):
            continue

        raw_data = yaml.safe_load(yml_file.read_text(encoding="utf-8")) or {}
        data = {str(k).strip().lower(): v for k, v in raw_data.items()}

        name = str(data.get("name") or "").strip()
        if not name:
            continue

        existing_img = str(data.get("image") or "").strip()
        if existing_img and "example.com" not in existing_img:
            continue

        print(f"Searching image for: {name}...")
        img_url = search_transparent_image(name)
        if not img_url:
            print(f"  [-] No transparent image found for '{name}'.")
            continue

        file_slug = slugify(name)
        saved_path = download_image(img_url, IMAGES_DIR / file_slug)
        if saved_path:
            # Store POSIX path (src/images/device-name.png) so GitHub renders it properly
            rel_path = saved_path.as_posix()
            update_yaml_image_field(yml_file, rel_path)
            print(f"  [+] Saved {rel_path} and updated {yml_file.name}")
            added_count += 1

    print(f"\nDone! Added {added_count} new device image(s).")

if __name__ == "__main__":
    main()
