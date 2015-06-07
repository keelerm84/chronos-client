# chronos-client

## Build the image (instructions given for OS X)

1. Download and copy the Raspbian image.

        sudo diskutil unmountDisk /dev/rdiskX
        sudo dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/rdiskX

2. Write it to an SD card and copy Chronos files into place:

        sudo diskutil mountDisk /dev/diskX
        cp -R chronos-client /Volumes/boot/chronos-client
        cp chronos-client/boot/config.txt /Volumes/boot/config.txt
        sudo diskutil unmountDisk /dev/diskX

3. Boot the new SD card image.  The `raspi-config` utility will appear on first
   boot.  Perform the following operations:

   - Select "1 Expand Filesystem"
   - Select "Finish"

4. The system will reboot.  Log in (default username is "pi" and password is
   "raspberry") and run the Chronos install script:

        /boot/chronos-client/install.sh

5. The system will reboot and Chronos will launch.
