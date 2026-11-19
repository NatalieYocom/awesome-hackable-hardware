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
        return "-"
    if not url.startswith(("http://", "https://")):
        url = f"https://{url}"
    return f"[{label}]({url})"

def get_category_heading(category_dir: pathlib.Path) -> str:
    name_file = category_dir / "foldername_"
    if name_file.exists():
        custom_name = name_file.read_text(encoding="utf-8").strip()
        if custom_name:
            return custom_name
    # Fallback if foldername_ is missing or empty
    return category_dir.name.replace("-", " ").title()

def build():
    if not TEMPLATE_FILE.exists():
        raise FileNotFoundError(f"Missing template file: {TEMPLATE_FILE}")

    template_content = TEMPLATE_FILE.read_text(encoding="utf-8")
    sections = []

    if DEVICES_DIR.exists():
        # Every subfolder inside src/devices/ becomes a category section
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
            lines = [
                f"## {heading}\n",
                "| Device | Type | Difficulty | Firmware | Reversible | Brick Risk | Tools | Links | Notes |",
                "| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |",
            ]

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
                    tools = ", ".join(cleaned_tools) if cleaned_tools else "-"
                else:
                    tools = str(raw_tools).strip() or "-"

                guide_link = format_link(d.get("guide"), "Guide")
                cfw_link = format_link(d.get("cfw"), "CFW")
                links = " • ".join(l for l in (guide_link, cfw_link) if l != "-") or "-"

                raw_notes = str(d.get("notes") or "-").strip()
                notes = "-" if raw_notes == "example" else raw_notes.replace("\n", " ").replace("|", "\\|")

                lines.append(
                    f"| **{name}** | {mod_type} | {diff} | {fw} | {reversible} | {brick} | {tools} | {links} | {notes} |"
                )

            sections.append("\n".join(lines))

    generated_tables = "\n\n".join(sections)

    if PLACEHOLDER in template_content:
        output = template_content.replace(PLACEHOLDER, generated_tables)
    else:
        output = template_content.rstrip() + "\n\n" + generated_tables + "\n"

    README_FILE.write_text(output, encoding="utf-8")
    print(f"Successfully generated {README_FILE} with {len(sections)} device categories.")

if __name__ == "__main__":
    build()
