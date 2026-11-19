name: Midea / Frigidaire / Toshiba / Insignia Air Conditioners & Dehumidifiers
type: Hardmod
difficulty: Easy
firmware: "1.0 - 3.0"
reversible: true
brick: none
tools:
- ESP8266 or ESP32 USB dongle (pre-flashed or DIY with USB-A female breakout)
- Phillips screwdriver (to open the front display bezel)
guide: https://esphome.io/components/climate/midea.html
cfw: https://github.com/mac-zhou/midea-ac-py
image:
notes: "Unplugs the factory Midea cloud Wi-Fi USB stick inside the unit's front panel and replaces it with an ESPHome dongle, giving instant local temperature, mode, and fan control in Home Assistant."
