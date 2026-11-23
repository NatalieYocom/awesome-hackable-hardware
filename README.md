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


## Categories

- [Video Game Consoles](#video-game-consoles) *(10 devices)*
- [Home Automation](#home-automation) *(5 devices)*
- [Household Appliances](#household-appliances) *(3 devices)*
- [Media Players](#media-players) *(4 devices)*

---

## Video Game Consoles

---

### Nintendo 3DS
<img src="src/images/nintendo-3ds.png" alt="Nintendo 3DS" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `1.0.0 - 11.17.0` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** SD card (4GB or larger), SD card reader, PC, Mac, or Android device, Magnet (only required for ntrboot method)
- **Links:** [📖 Guide](https://3ds.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/LumaTeam/Luma3DS)
- **Notes:** Supports all models (Old 3DS, 2DS, New 3DS, New 2DS XL). MSET9 and super-skaterhax cover the latest firmwares.

---

### Nintendo DSi
<img src="src/images/nintendo-dsi.jpeg" alt="Nintendo DSi" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `1.4 - 1.4.5` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** SD card (2GB or larger, FAT32 formatted), SD card reader, PC or Mac
- **Links:** [📖 Guide](https://dsi.cfw.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/DS-Homebrew/TWiLightMenu)
- **Notes:** Uses the Memory Pit exploit via the Nintendo DSi Camera app, followed by Unlaunch for coldbooting directly into TWiLight Menu++.

---

### Nintendo Switch (OLED / Lite / V2)
<img src="src/images/switch.png" alt="Nintendo Switch (OLED / Lite / V2)" height="140" />

> **Type:** `Hardmod` &nbsp;|&nbsp; **Difficulty:** 🔴 Difficult &nbsp;|&nbsp; **Firmware:** `1.0.0 - 19.0.1` &nbsp;|&nbsp; **Reversible:** No &nbsp;|&nbsp; **Brick Risk:** 🔴 Likely

- **Tools:** Picofly (RP2040) or Instinct-NX modchip, Soldering iron with fine tip and flux, Microscope or magnifying glass, Tri-wing and Phillips, microSD card
- **Links:** [📖 Guide](https://switch.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/Atmosphere-NX/Atmosphere)
- **Notes:** Requires micro-soldering directly to motherboard capacitors and flex cables. OLED models require the DAT0 adapter or Kamikaze method.

---

### Nintendo Switch (Unpatched V1)
<img src="src/images/switch.png" alt="Nintendo Switch (Unpatched V1)" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `1.0.0 - 19.0.1` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** RCM Jig, USB-C to USB-A/C data cable, microSD card (64GB or larger recommended), PC, Mac, or Android phone (payload injector)
- **Links:** [📖 Guide](https://switch.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/Atmosphere-NX/Atmosphere)
- **Notes:** Only applies to early Erista (V1) units manufactured before mid-2018 vulnerable to the Fusee Gelee exploit. Newer Switch models require a modchip.

---

### Nintendo Wii
<img src="src/images/wii.png" alt="Nintendo Wii" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `4.3` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** SD card (2GB or larger, formatted to FAT32), SD card reader, Internet connection (for str2hax DNS exploit)
- **Links:** [📖 Guide](https://wii.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/HomebrewChannel/hbc)
- **Notes:** Can be modded using LetterBomb (requires MAC address and SD card) or str2hax (requires no SD card initially, only a DNS change).

---

### Nintendo Wii U
<img src="src/images/wiiu.jpeg" alt="Nintendo Wii U" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `5.5.0 - 5.5.6` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** SD card (32GB or larger recommended, FAT32 formatted), SD card reader, PC or Mac
- **Links:** [📖 Guide](https://wiiu.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/wiiu-env/Aroma)
- **Notes:** Uses the browser-based JS Type Confusion exploit to install Aroma CFW and PayloadLoader for coldboot functionality.

---

### PlayStation 4
<img src="src/images/ps4.png" alt="PlayStation 4" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `1.00 - 11.00` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** USB flash drive (exFAT formatted), Ethernet cable and PC (required for 9.03 - 11.00 PPPwn exploit)
- **Links:** [📖 Guide](https://consolemods.org/wiki/PS4:PS4_Mods_Wiki) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/GoldHEN/GoldHEN)
- **Notes:** Jailbreak is tethered and must be re-applied after a full reboot. Firmware 9.00 uses a USB/WebKit exploit; 11.00 uses the PPPwn Ethernet exploit.

---

### PlayStation Vita
<img src="src/images/vita.png" alt="PlayStation Vita" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `3.60 - 3.74` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** Internet connection (for HENlo browser exploit), Official Sony Memory Card (required for OLED 1000 models), SD2Vita adapter + microSD card (recommended for storage)
- **Links:** [📖 Guide](https://vita.hacks.guide) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/TheOfficialFloW/henkaku)
- **Notes:** Firmware 3.74 can be hacked directly via the built-in web browser without a PC, then downgraded to 3.65 for permanent Enso CFW.

---

### Sony PlayStation 3
<img src="src/images/ps3.png" alt="Sony PlayStation 3" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `4.80 - 4.91` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** USB flash drive (FAT32 formatted), PC or Mac, Internet connection on the PS3
- **Links:** [📖 Guide](https://consolemods.org/wiki/PS3:PS3_Mods_Wiki) &nbsp;•&nbsp; [⚙️ CFW](https://www.psx-place.com/forums/ps3-jailbreak-cfw-and-ps3hen.86/)
- **Notes:** Fat models and early Slim models (CECH-20xx to 25xx) support full CFW (Evilnat). Late Slims and Super Slims only support PS3HEN.

---

### Sony PlayStation Portable (PSP)
<img src="src/images/psp.png" alt="Sony PlayStation Portable (PSP)" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `6.60 - 6.61` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** Memory Stick PRO Duo (or microSD to Memory Stick adapter), Mini-USB cable or card reader, PC or Mac
- **Links:** [📖 Guide](https://www.pspunk.com/psp-cfw/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/PSP-Archive/ARK-4)
- **Notes:** All PSP models (1000, 2000, 3000, Go, Street) can run permanent ARK-4 CFW via Infinity or cIPL.

<br>

## Home Automation

---

### Amazon Echo Dot (2nd Gen)
<img src="src/images/alexagen2.png" alt="Amazon Echo Dot (2nd Gen)" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `FireOS 5 - FireOS 6` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🔴 Likely

- **Tools:** Micro-USB data cable, Linux or Windows PC, ADB and Fastboot tools, amonet exploit package
- **Links:** [📖 Guide](https://xdaforums.com/t/unlock-root-twrp-unbrick-amazon-echo-dot-2nd-gen-2016-biscuit.4761416/) &nbsp;•&nbsp; [⚙️ CFW](https://danieldb.uk/posts/alexa-2/)
- **Notes:** Exploits the MediaTek bootrom (amonet/kamakiri) to unlock the bootloader, flash TWRP recovery, and gain root shell access over ADB. Many solutions with this unlock.

---

### Google Nest Learning Thermostat (Gen 1 / Gen 2)
<img src="src/images/nest.png" alt="Google Nest Learning Thermostat (Gen 1 / Gen 2)" height="140" />

> **Type:** `Hardmod` &nbsp;|&nbsp; **Difficulty:** 🔴 Difficult &nbsp;|&nbsp; **Firmware:** `1.0 - 5.9` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🔴 Likely

- **Tools:** Torx T5 screwdriver, Plastic spudger / pry tool, Micro-USB cable (for DFU / omap_loader mode), Linux PC or Raspberry Pi
- **Links:** [📖 Guide](https://github.com/codykociemba/NoLongerEvil-Thermostat) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/codykociemba/NoLongerEvil-Thermostat)
- **Notes:** Bypasses Google's discontinued cloud servers on older Nest units via USB DFU mode to inject a custom Linux kernel and local API, restoring local control and Home Assistant integration.

---

### Roborock / Dreame / Xiaomi Robot Vacuums
<img src="src/images/roborock.webp" alt="Roborock / Dreame / Xiaomi Robot Vacuums" height="140" />

> **Type:** `Hardmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `1.0.0 - 4.3.9` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** Varies per vaccum, see guide.
- **Links:** [📖 Guide](https://valetudo.cloud/pages/general/getting-started.html) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/Hypfer/Valetudo)
- **Notes:** Replaces the vendor cloud with Valetudo, providing a completely local web interface, room mapping, and native MQTT integration for Home Assistant without sending floorplans to external servers.

---

### Wyze Cam (v2 / v3 / Pan v1 / Pan v2)
<img src="src/images/wyze.png" alt="Wyze Cam (v2 / v3 / Pan v1 / Pan v2)" height="140" />

> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `4.9.1 - 4.36.11` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** microSD card (32GB or smaller, FAT32 formatted), microSD card reader, PC or Mac
- **Links:** [📖 Guide](https://thingino.com/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/themactep/thingino-firmware)
- **Notes:** Boots from a microSD card (or flashes directly to SPI NOR flash) to replace Wyze's cloud-dependent firmware with Thingino, unlocking local RTSP streams, ONVIF, and MQTT for Frigate and Home Assistant.

---

### Xiaomi LYWSD03MMC Temperature & Humidity Sensor
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `1.0.0_0109 - 2.1.1_0159` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** PC, Mac, or Android phone with Bluetooth, Chrome or Edge browser (for Web Bluetooth Telink Flasher)
- **Links:** [📖 Guide](https://github.com/pvvx/ATC_MiThermometer) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/pvvx/ATC_MiThermometer)
- **Notes:** Flashes wirelessly over Bluetooth Low Energy directly from a browser. Removes Xiaomi Mi Home cloud encryption, adds custom BTHome/Zigbee advertising formats, and extends battery life.

<br>

## Household Appliances

---

### LG Smart TVs (webOS)
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `3.0.0 - 24.20.0` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** Local Wi-Fi network, PC, Mac, or Linux machine (running webOS Dev Manager), LG Developer Mode account (or browser exploit via RootMyTV / DejaVu)
- **Links:** [📖 Guide](https://www.webosbrew.org/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/webosbrew/homebrew-channel)
- **Notes:** Installs the webOS Homebrew Channel, enabling ad-free YouTube (YouTube AdFree), Hyperion ambient lighting capture, SSH root access, and full local Home Assistant control without LG cloud telemetry.

---

### Samsung Smart TVs (Tizen OS)
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `1000 - 2500` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** PC or Mac (running Tizen Studio or TizenBrew), Local Wi-Fi network, Samsung Developer Mode enabled on TV
- **Links:** [📖 Guide](https://github.com/reisxd/TizenBrew) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/reisxd/TizenTube)
- **Notes:** Uses Developer Mode to sideload TizenBrew and custom web apps (such as TizenTube for ad-free playback and MoonLight for game streaming) while allowing local WebSocket control in Home Assistant with Samsung's ad/telemetry domains blocked via Pi-hole.

---

### Smart Life / Tuya Wi-Fi Devices (ESP8266 / BK7231)
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `1.0.0 - 2.9.0` &nbsp;|&nbsp; **Reversible:** No &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** Linux PC or Raspberry Pi with a Wi-Fi adapter, Secondary smartphone or laptop (to join the dummy AP)
- **Links:** [📖 Guide](https://github.com/tuya-cloudcutter/tuya-cloudcutter) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/arendst/Tasmota)
- **Notes:** Uses pre-built tuya-cloudcutter profiles and existing Tasmota/OpenBeken firmware images to flash Tuya-based devices (like HoneyGuaridan or Petlibro Wi-Fi pet feeders) over the air with images that allow full local control.

<br>

## Media Players

---

### Amazon Fire TV Stick (4K / Lite / Gen 2 / Gen 3)
> **Type:** `Hardmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `5.2.6.0 - 7.6.6.8` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** Aluminum foil or fine tweezers (to short the CLK/DAT resistor to GND), Plastic spudger / pry tool (to open the stick casing), Micro-USB data cable, Linux PC or Raspberry Pi (running kamakiri / amonet exploit scripts)
- **Links:** [📖 Guide](https://xdaforums.com/c/amazon-fire-tv.3075/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/Rortiz2/LineageOS-FireTV)
- **Notes:** Uses a BootROM exploit (kamakiri/amonet) by briefly shorting a motherboard test point during USB connection to unlock the bootloader, allowing TWRP recovery, Magisk root, custom launchers, and blocking Amazon OTA updates.

---

### Google Chromecast with Google TV (HD / 4K)
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `10.0 - 12.0` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** USB-C hub with Power Delivery, USB-A to USB-A data cable (or Linux PC for DirtyCow / bootloader unlock), PC or Mac (with ADB and Fastboot)
- **Links:** [📖 Guide](https://xdaforums.com/f/chromecast-with-google-tv.12257/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/topjohnwu/Magisk)
- **Notes:** Early unpatched firmware versions allow bootloader unlocking via the Amlogic exploit, enabling LineageOS or de-Googled stock firmware with custom launchers and local ADB control from Home Assistant.

---

### Linkplay Audio Modules (WiiM / Arylic / Audio Pro / GGMM)
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟡 Intermediate &nbsp;|&nbsp; **Firmware:** `3.6 - 4.6` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟡 Unlikely

- **Tools:** PC or Mac (with SSH / Telnet / curl), Local Wi-Fi or Ethernet network
- **Links:** [📖 Guide](https://github.com/AndersFluur/LinkPlayApi) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/nicjo814/home-assistant-linkplay)
- **Notes:** Exposes undocumented local HTTP/HTTPS APIs and root telnet/SSH shells on Linkplay-based streamers, allowing multi-room grouping, TTS announcements, and playback control in Home Assistant with WAN internet access blocked at the router.

---

### Roku Streaming Players & Roku TVs
> **Type:** `Softmod` &nbsp;|&nbsp; **Difficulty:** 🟢 Easy &nbsp;|&nbsp; **Firmware:** `9.0 - 13.1` &nbsp;|&nbsp; **Reversible:** Yes &nbsp;|&nbsp; **Brick Risk:** 🟢 None

- **Tools:** Web browser, Local Wi-Fi network, Home Assistant instance
- **Links:** [📖 Guide](https://www.home-assistant.io/integrations/roku/) &nbsp;•&nbsp; [⚙️ CFW](https://github.com/iamkubi/roku-developer-mode)
- **Notes:** Enabling secret Developer Mode allows sideloading custom BrightScript apps and exposes the local External Control Protocol (ECP) REST API on port 8060, enabling full Home Assistant automation even when Roku cloud servers are blocked.

---

## Contributing

1. Fork the repository and create a new branch.
2. Copy `template.yml` into the matching category folder inside `src/devices/` (e.g., `src/devices/handhelds/my-device.yml`).
3. Fill out all required fields using valid YAML syntax. Ensure all URLs start with `https://`.
4. Open a Pull Request with a brief summary of your addition or update.

## Disclaimer

All hardware and software modifications carry inherent risk. **Always verify your exact model number, board revision, and current firmware version** before running exploits or flashing custom firmware. Neither the maintainers nor contributors are responsible for bricked devices, voided warranties, or banned online accounts.
