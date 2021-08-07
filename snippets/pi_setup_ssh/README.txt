For the pizero to be able to communicate via ssh, we need to enable and configure it

The way to do this:

-download raspberry pi flasher
-install raspberry pi OS on a micro SD card (I use the lite version for pizero)
-copy the "ssh" and "wpa_supplicant.conf" files to the root directory of the SD card
-edit the wpa_supplicant.conf file to contain the correct network name and password for the wifi connection being used
-make sure both files are saved as typless, or "ALL TYPES" without any extensions