# Moddable & Homebrewable Devices

An index of devices that can be modified or hacked to do what you want it to!

> **Want to add a device?** Copy `template.yml` into the matching category folder inside `src/devices/` and open a Pull Request!

## Video Game Consoles

---

### Nintendo 3DS
**Type:** Softmod · **Difficulty:** Easy · **Firmware:** 1.0.0 - 11.17.0 · **Reversible:** Yes · **Brick Risk:** Unlikely
* **Tools:** SD card (4GB or larger), SD card reader, PC, Mac, or Android device, Magnet (only required for ntrboot method)
* **Links:** [Guide](https://3ds.hacks.guide) • [CFW](https://github.com/LumaTeam/Luma3DS)
* **Notes:** Supports all models (Old 3DS, 2DS, New 3DS, New 2DS XL). MSET9 and super-skaterhax cover the latest firmwares.

---

### Nintendo Switch (Unpatched V1)
**Type:** Softmod · **Difficulty:** Intermediate · **Firmware:** 1.0.0 - 19.0.1 · **Reversible:** Yes · **Brick Risk:** Unlikely
* **Tools:** RCM Jig, USB-C to USB-A/C data cable, microSD card (64GB or larger recommended), PC, Mac, or Android phone (payload injector)
* **Links:** [Guide](https://switch.hacks.guide) • [CFW](https://github.com/Atmosphere-NX/Atmosphere)
* **Notes:** Only applies to early Erista (V1) units manufactured before mid-2018 vulnerable to the Fusee Gelee exploit. Newer Switch models require a modchip.

---

### Nintendo Wii
**Type:** Softmod · **Difficulty:** Easy · **Firmware:** 4.3 · **Reversible:** Yes · **Brick Risk:** Unlikely
* **Tools:** SD card (2GB or larger, formatted to FAT32), SD card reader, Internet connection (for str2hax DNS exploit)
* **Links:** [Guide](https://wii.hacks.guide) • [CFW](https://github.com/HomebrewChannel/hbc)
* **Notes:** Can be modded using LetterBomb (requires MAC address and SD card) or str2hax (requires no SD card initially, only a DNS change).

---

### PlayStation Vita
**Type:** Softmod · **Difficulty:** Easy · **Firmware:** 3.60 - 3.74 · **Reversible:** Yes · **Brick Risk:** Unlikely
* **Tools:** Internet connection (for HENlo browser exploit), Official Sony Memory Card (required for OLED 1000 models), SD2Vita adapter + microSD card (recommended for storage)
* **Links:** [Guide](https://vita.hacks.guide) • [CFW](https://github.com/TheOfficialFloW/henkaku)
* **Notes:** Firmware 3.74 can be hacked directly via the built-in web browser without a PC, then downgraded to 3.65 for permanent Enso CFW.

## Home Automation

---

### Echo Dot 2nd Gen
<img src="src/images/alexagen2.png" alt="Echo Dot 2nd Gen" height="140" />

**Type:** Softmod · **Difficulty:** Easy · **Firmware:** any · **Reversible:** Yes · **Brick Risk:** Unlikely
* **Tools:** USB Cable, Computer
* **Links:** [Guide](https://github.com/Gamer92000/echo-dot-assist)
* **Notes:** Requires a working Home Assistant server and pipeline.

## Contributing & Disclaimer
All modifications carry inherent risk. Always double-check your exact hardware revision before flashing firmware.
