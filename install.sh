#!/bin/sh

cd "$(dirname "$0")"

# Copy boot config
sudo cp ./etc/config.txt /boot/config.txt

# Copy wpa_supplicant information
sudo cp ./etc/wpa.conf /etc/wpa_supplicant/wpa_supplicant.conf

# Install PiTFT helper
# This is required for the Adafruit TFT w/ Touch Screen
#
# curl -SLs https://apt.adafruit.com/add | sudo bash
# sudo apt-get install -y raspberrypi-bootloader-adafruit-pitft
# sudo apt-get install -y adafruit-pitft-helper
# sudo adafruit-pitft-helper -t 35r

# Start Chronos at boot
sudo cp ./etc/51-override-startup /etc/X11/Xsession.d/51-override-startup
sudo cp ./etc/rc.local /etc/rc.local

sudo reboot
