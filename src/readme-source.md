# Moddable & Homebrewable Devices

A community-maintained index of consoles, handhelds, and hardware that can be jailbroken, softmodded, or hardmodded to run custom firmware (CFW) and homebrew software.

> **Want to add or update a device?**
> Do **not** edit `README.md` directly—it is automatically generated. Instead, copy `template.yml` into the appropriate category folder under `src/devices/` and submit a Pull Request.

> [!NOTE]
> If you encounter an issue (broken link, improper documentation) submit an issue.

---

## Understanding the Fields

Each device entry tracks key requirements and risk levels before you begin:

* **Type:** `Softmod` (software-only exploit) or `Hardmod` (requires physical hardware modification or soldering).
* **Difficulty:** `Easy` (beginner-friendly, drag-and-drop files), `Intermediate` (requires specific hardware revisions, payloads, or multi-step downgrades), or `Difficult` (micro-soldering or high-precision hardware work).
* **Firmware:** Supported system software versions.
* **Reversible:** Whether the device can be cleanly restored to stock firmware.
* **Brick Risk:** Likelihood of permanently damaging the device if steps are followed incorrectly (`none`, `unlikely`, or `likely`).


{{DEVICES}}

---

## Contributing

1. Fork the repository and create a new branch.
2. Copy `template.yml` into the matching category folder inside `src/devices/` (e.g., `src/devices/handhelds/my-device.yml`).
3. Fill out all required fields using valid YAML syntax. Ensure all URLs start with `https://`.
4. Open a Pull Request with a brief summary of your addition or update.

## Disclaimer

All hardware and software modifications carry inherent risk. **Always verify your exact model number, board revision, and current firmware version** before running exploits or flashing custom firmware. Neither the maintainers nor contributors are responsible for bricked devices, voided warranties, or banned online accounts.
