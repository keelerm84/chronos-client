#!/bin/sh

cd "$(dirname "$0")"

# Copy boot config
sudo cp ./etc/config.txt /boot/config.txt

# Copy wpa_supplicant information
sudo cp ./etc/wpa.conf /etc/wpa_supplicant/wpa_supplicant.conf

sudo reboot
