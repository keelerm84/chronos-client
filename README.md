# chronos-client

## Build the image

1. Download the Raspbian image.

2. Write it to an SD card and then boot.

        sudo diskutil unmountDisk /dev/disk2
        sudo dd bs=1m if=2015-05-05-raspbian-wheezy.img of=/dev/disk2
