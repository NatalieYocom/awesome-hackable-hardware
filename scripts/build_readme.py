import pathlib
import re
import yaml

SRC_DIR = pathlib.Path("src")
DEVICES_DIR = SRC_DIR / "devices"
TEMPLATE_FILE = SRC_DIR / "readme-source.md"
README_FILE = pathlib.Path("README.md")
PLACEHOLDER = "{{DEVICES}}"
TOC_PLACEHOLDER = "{{TOC}}"

DIFFICULTY_BADGES = {
    "trivial": "🟢 Trivial",
    "easy": "🟢 Easy",
    "intermediate": "🟡 Intermediate",
    "difficult": "🔴 Difficult",
    "hard": "🔴 Hard",
}

BRICK_BADGES = {
    "none": "🟢 None",
    "unlikely": "🟡 Unlikely",
    "likely": "🔴 Likely",
}

def slugify(text: str) -> str:
    """Matches GitHub's exact heading anchor generation rules."""
    slug = text.strip().lower()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"\s+", "-", slug)
    return slug

def format_link(raw_url: str, label: str) -> str:
    url = str(raw_url or "").strip()
    if not url or "example.com" in url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return f"[{label}]({url})"

def format_image(raw_img: str, alt_text: str) -> str:
    img = str(raw_img or "").strip()
    if not img or "example.com" in img:
        return ""
    return f'<img src="{img}" alt="{alt_text}" height="140" />'

def format_difficulty(raw_diff: str) -> str:
    val = str(raw_diff or "").strip()
    if not val or val == "-":
        return "-"
    return DIFFICULTY_BADGES.get(val.lower(), val.capitalize())

def format_brick(raw_brick: str) -> str:
    val = str(raw_brick or "").strip()
    if not val or val == "-":
        return "-"
    return BRICK_BADGES.get(val.lower(), val.capitalize())

def get_category_heading(category_dir: pathlib.Path) -> str:
    name_file = category_dir / "foldername_"
    if name_file.exists():
        custom_name = name_file.read_text(encoding="utf-8").strip()
        if custom_name:
            return custom_name
    return category_dir.name.replace("-", " ").title()

def build():
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Missing template file: {TEMPLATE_FILE}")

    template_content = TEMPLATE_FILE.read_text(encoding="utf-8")
    categories_data = []

    if DEVICES_DIR.exists():
        for category_dir in sorted(p for p in DEVICES_DIR.iterdir() if p.is_dir()):
            devices = []
            for yml_file in sorted(category_dir.glob("*.yml")):
                if yml_file.name.startswith("_"):
                    continue
                with open(yml_file, "r", encoding="utf-8") as f:
                    raw_data = yaml.safe_load(f) or {}
                    # Normalize keys to lowercase so capitalization/spaces never break fields
                    data = {str(k).strip().lower(): v for k, v in raw_data.items()}
                    if data.get("name"):
                        devices.append(data)

            if not devices:
                continue

            devices.sort(key=lambda d: str(d.get("name", "")).lower())
            heading = get_category_heading(category_dir)
            categories_data.append((heading, devices))

    # Build clickable Table of Contents
    toc_lines = ["## Categories\n"]
    for heading, devices in categories_data:
        anchor = slugify(heading)
        count = len(devices)
        label = "device" if count == 1 else "devices"
        toc_lines.append(f"- [{heading}](#{anchor}) *({count} {label})*")
    toc_block = "\n".join(toc_lines)

    # Build formatted category sections
    sections = []
    for heading, devices in categories_data:
        category_blocks = [f"## {heading}"]

        for d in devices:
            name = str(d.get("name", "Unknown")).strip()
            mod_type = str(d.get("type") or "-").strip()
            diff = format_difficulty(d.get("difficulty"))
            fw = str(d.get("firmware") or "-").strip()

            rev_val = d.get("reversible")
            if isinstance(rev_val, str):
                rev_val = rev_val.strip().lower() in ("true", "yes", "1")
            reversible = "Yes" if rev_val is True else ("No" if rev_val is False else "-")

            brick = format_brick(d.get("brick"))

            raw_tools = d.get("tools") or []
            if isinstance(raw_tools, list):
                cleaned_tools = [
                    str(t).strip()
                    for t in raw_tools
                    if str(t).strip() not in ("", "tool 1", "tool 2", "tool 3")
                ]
                tools = ", ".join(cleaned_tools)
            else:
                tools = str(raw_tools).strip()

            guide_link = format_link(d.get("guide"), "📖 Guide")
            cfw_link = format_link(d.get("cfw"), "⚙️ CFW")
            links = " &nbsp;•&nbsp; ".join(l for l in (guide_link, cfw_link) if l)

            raw_notes = str(d.get("notes") or "").strip()
            notes = "" if raw_notes == "example" else raw_notes.replace("\n", " ")

            image_tag = format_image(d.get("image"), name)

            card = [f"### {name}"]
            if image_tag:
                card.append(image_tag + "\n")

            card.append(
                f"> **Type:** `{mod_type}` &nbsp;|&nbsp; "
                f"**Difficulty:** {diff} &nbsp;|&nbsp; "
                f"**Firmware:** `{fw}` &nbsp;|&nbsp; "
                f"**Reversible:** {reversible} &nbsp;|&nbsp; "
                f"**Brick Risk:** {brick}\n"
            )

            if tools:
                card.append(f"- **Tools:** {tools}")
            if links:
                card.append(f"- **Links:** {links}")
            if notes:
                card.append(f"- **Notes:** {notes}")

            category_blocks.append("\n".join(card))

        sections.append("\n\n---\n\n".join(category_blocks))

    generated_devices = "\n\n<br>\n\n".join(sections)

    # Inject TOC and Devices into readme-source.md
    output = template_content
    if TOC_PLACEHOLDER in output:
        output = output.replace(TOC_PLACEHOLDER, toc_block)
    else:
        # Automatically place TOC right above {{DEVICES}} if {{TOC}} wasn't specified
        generated_devices = f"{toc_block}\n\n---\n\n{generated_devices}"

    if PLACEHOLDER in output:
        output = output.replace(PLACEHOLDER, generated_devices)
    else:
        output = output.rstrip() + "\n\n" + generated_devices + "\n"

    README_FILE.write_text(output, encoding="utf-8")
    print(f"Successfully generated {README_FILE} with {len(categories_data)} categories.")

if __name__ == "__main__":
    build()
