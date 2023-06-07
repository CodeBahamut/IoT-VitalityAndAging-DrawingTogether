# Storage Configuration


## Issue that leads having 24GB instead of 64GB
When downloading the "jetbot-043_nano-4gb-jp45.zip" from v0.4.3 for jetbot (Jetson Nano (4GB)), and flash it by etcher successfully. But when the jJetbot is powered, only 
24G storage is available.
So to solve this issue please follow the given steps.

1. Download the pre-built JetBot SD card image
   Download the pre-built JetBot SD card image from the table below. Make sure to select the version that matches the
   Jetson you're using (for example Jetson Nano 2GB).

| Platform          | JetPack version | Jetbot version |                                                Response                                                |           MD5 Checksum           |
|:------------------|:----------------|:---------------|:------------------------------------------------------------------------------------------------------:|:--------------------------------:|
| Jetson Nano (4GB) | 4.5             | 0.4.3          | [jetbot-043_nano-4gb-jp45.zip](https://drive.google.com/file/d/1o08RPDRZuDloP_o76tCoSngvq1CVuCDh/view) | 760b1885646bfad8590633acca014289 |


!!! warning
    To utilize one of the JetBot SD card images based on JetPack 4.5, start your Jetson Nano with a plain JetPack 4.5 SD card image and go through the operating system setup. This will do a one-time setting that will allow you to utilize JetPack 4.5 SD card images on your device. Original JetPack SD card pictures may be found here: JetPack SD card image for Jetson Nano 2GB and JetPack SD card image for Jetson Nano (4GB). After you've completed this method, you may utilize the JetPack 4.5-based JetBot SD card images provided above on your device.


2. Flash JetBot image onto SD card
   Insert an SD card into your desktop machine

Using Etcher, select the image you downloaded above and flash it onto the SD card.

Remove the SD card from your desktop machine

3. Boot Jetson Nano
    - Insert the SD card into your Jetson Nano (the micro SD card slot is located under the module)
    - Connect the monitor, keyboard, and mouse to the Nano
    - Power on the Jetson Nano by connecting the micro USB (for Jetson Nano (4GB)) or USB-C (for Jetson Nano 2GB)
      charger to the port

!!! warning
    We recommend that you initially start the Jetson Nano without the piOLED or motor driver attached.
    This manner, you can ensure that the system boots successfully from the SD card image without having to worry about hardware concerns. After confirming that it boots, reattach the piOLED, double-check your wiring, and reboot.

!!! note
    Make sure that you have downloaded this Jetson Nano image: jetbot-043_nano-4gb-jp45.zip, the official documentation recommends other version which is 4.5.

4. Now you have to execute some commands
    - Go to Jetcard directory
      ```bash
      cd ~/jetcard
      ```
    - Pull the latest changes by executing this command
      ```bash
      git pull
      ```
    - Lastly, execute the pulled bash script
      ```bash
      ./script/jetson_install_nvresizefs_service.sh
      ```

To check whether the Jetbot is using the full size of the SD card, which is 64GB, run this command in the terminal<br>
```bash
df -h
```
you should see something like this

```bash
jetbot@nano-4gb-jp45:~$ df -h
Filesystem Size Used Avail Use% Mounted on
/dev/mmcblk0p1 64G 25G 35G 39% /
none 1.8G 0 1.8G 0% /dev
tmpfs 2.0G 4.0K 2.0G 1% /dev/shm
tmpfs 2.0G 19M 2.0G 1% /run
tmpfs 5.0M 4.0K 5.0M 1% /run/lock
tmpfs 2.0G 0 2.0G 0% /sys/fs/cgroup
tmpfs 397M 0 397M 0% /run/user/1000
```
