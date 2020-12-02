# Rotary Dial Phone

## Setup
1. Install Raspberry Pi OS Light, e.g. via Raspberry Pi Imager
2. In /boot partition on SD card add line `enable_uart=1` in config.txt
3. Login to uart console with baudrate 11520 (connect Gnd and both Uart Pins via USB2Serial Adapter). Login is `pi` pw `raspberry`
4. Run `raspi-config` go to network settings and setup wifi connection that is available in the house, make sure to enable a supported network (for me only 2.4GHz worked) to test this run the following command to find the SSID of all supported networks
```
iw wlan0 scan | grep ESSID
```
5. Run `sudo apt-get update`
6. Install `gpiozero`
```
sudo apt install python3-gpiozero
```



7. Blacklist audio output and enable usb audio as card 0
sudo nano /etc/modprobe.d/alsa-base.conf
```
options snd-usb-audio index=0
blacklist snd_bcm2835
```

8. Install the mumble client [talkkonnect](https://github.com/talkkonnect/talkkonnect)
 * Install as described in the README
 * It should be possible to distribute the binary alongside the config file among other raspberry zero devices
 * Use the supplied config `talkkclient.xml` adapt it and launch the application via
 ```
 ./bin/talkkonnect --config talkkonnect.xml
 ```

 

## TODOs
- Test GPIO pins
- Check if any GPIO pins have built in pullup/pulldown
- Test USB audio

## References
[python3-gpiozero](https://gpiozero.readthedocs.io/en/v1.3.1/api_other.html)

