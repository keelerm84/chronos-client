# chronos-client

## Build the image

1. Download the Raspbian image.

2. Write it to an SD card and copy Chronos files into place:

        sudo diskutil unmountDisk /dev/rdiskX
        sudo dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/rdiskX

        sudo diskutil mountDisk /dev/diskX
        cp -R chronos-client /Volumes/boot/chronos-client
        cp chronos-client/boot/config.txt /Volumes/boot/chronos-client/boot/config.txt
        sudo diskutil unmountDisk /dev/diskX

3. Boot the new SD card image.  The `raspi-config` utility will appear on first
   boot.  Perform the following operations:

   - Select "1 Expand Filesystem"

   - Select "4 Internationalisation Options"
     Select "I1 Change Locale"
     - Disable "en.GB.UTF-8 UTF-8"
     - Enable "en.US.UTF-8 UTF-8"
     - Set "en.US.UTF-8 UTF-8" as the default locale

   - Select "8 Advanced Options"
     Enable "A4 SSH"

4. The system will reboot.  Log in (default username is "pi" and password is
   "raspberry") and run the Chronos install script:

        /boot/chronos-client/install.sh

5. The system will reboot and Chronos will launch.
