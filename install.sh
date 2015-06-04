#!/bin/sh

# Copy wpa_supplicant information
sudo cp ./etc/wpa.conf /etc/wpa_supplicant/wpa_supplicant.conf

# Install PiTFT helper
curl -SLs https://apt.adafruit.com/add | sudo bash
sudo apt-get install -y raspberrypi-bootloader-adafruit-pitft
sudo apt-get install -y adafruit-pitft-helper
sudo adafruit-pitft-helper -t 28r

# Start the UI at boot
cp ./etc/51-override-startup /etc/X11/Xsession.d/51-override-startup
