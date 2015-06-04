# chronos-client

## Build the image

1. Download the Raspbian image.

2. Write it to an SD card.

        sudo diskutil unmountDisk /dev/rdisk2
        sudo dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/rdisk2

3. Mount the SD card.

        sudo diskutil mountDisk /dev/disk2
        cp -R chronos-client /Volumes/boot/chronos-client
        sudo diskutil unmountDisk /dev/disk2

4. Boot the new SD card image.

5. Run `/boot/chronos-client/install-part-1.sh`.

6. Run `/boot/chronos-client/install-part-2.sh`.
