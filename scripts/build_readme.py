import pathlib
import yaml

SRC_DIR = pathlib.Path("src")
DEVICES_DIR = SRC_DIR / "devices"
TEMPLATE_FILE = SRC_DIR / "readme-source.md"
README_FILE = pathlib.Path("README.md")
PLACEHOLDER = "{{DEVICES}}"

def format_link(raw_url: str, label: str) -> str:
    url = str(raw_url or "").strip()
    if not url or "example.com" in url:
        return ""
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return f"[{label}]({url})"

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
    sections = []

    if DEVICES_DIR.exists():
        for category_dir in sorted(p for p in DEVICES_DIR.iterdir() if p.is_dir()):
            devices = []
            for yml_file in sorted(category_dir.glob("*.yml")):
                if yml_file.name.startswith("_"):
                    continue
                with open(yml_file, "r", encoding="utf-8") as f:
                    data = yaml.safe_load(f) or {}
                    if data.get("name"):
                        devices.append(data)

            if not devices:
                continue

            devices.sort(key=lambda d: str(d.get("name", "")).lower())

            heading = get_category_heading(category_dir)
            category_blocks = [f"## {heading}"]

            for d in devices:
                name = str(d.get("name", "Unknown")).strip()
                mod_type = str(d.get("type") or "-").strip()
                diff = str(d.get("difficulty") or "-").strip()
                fw = str(d.get("firmware") or "-").strip()

                rev_val = d.get("reversible")
                reversible = "Yes" if rev_val is True else ("No" if rev_val is False else "-")
                brick = str(d.get("brick") or "-").strip().capitalize()

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

                guide_link = format_link(d.get("guide"), "Guide")
                cfw_link = format_link(d.get("cfw"), "CFW")
                links = " • ".join(l for l in (guide_link, cfw_link) if l)

                raw_notes = str(d.get("notes") or "").strip()
                notes = "" if raw_notes == "example" else raw_notes.replace("\n", " ")

                # Build clean full-width device block
                card = [
                    f"### {name}",
                    f"**Type:** {mod_type} · **Difficulty:** {diff} · **Firmware:** {fw} · **Reversible:** {reversible} · **Brick Risk:** {brick}",
                ]
                if tools:
                    card.append(f"* **Tools:** {tools}")
                if links:
                    card.append(f"* **Links:** {links}")
                if notes:
                    card.append(f"* **Notes:** {notes}")

                category_blocks.append("\n".join(card))

            sections.append("\n\n---\n\n".join(category_blocks))

    generated_content = "\n\n".join(sections)

    if PLACEHOLDER in template_content:
        output = template_content.replace(PLACEHOLDER, generated_content)
    else:
        output = template_content.rstrip() + "\n\n" + generated_content + "\n"

    README_FILE.write_text(output, encoding="utf-8")
    print(f"Successfully generated {README_FILE} with {len(sections)} device categories.")

if __name__ == "__main__":
    build()
