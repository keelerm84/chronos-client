#!/bin/sh

# Install PiTFT helper
curl -SLs https://apt.adafruit.com/add | sudo bash
sudo apt-get install -y raspberrypi-bootloader-adafruit-pitft
sudo apt-get install -y adafruit-pitft-helper
sudo adafruit-pitft-helper -t 35r

# Start the UI at boot
sudo cp ./etc/51-override-startup /etc/X11/Xsession.d/51-override-startup

sudo reboot
