![DoorPi](http://wellsosaur.us/YIA6/Untitled%20Sketch_bb.png)

# DoorPi

Plays a chime when the Envoy front door is opened.

## Requirements

* RPi GPIO library
* [Pygame](http://www.pygame.org)
* Raspberry Pi (we used Adafruit Raspberry Pi Rev. B+)
* Internet connection (wired or wireless, for remote debugging)
* [Reed Switch](https://www.adafruit.com/products/375) on GPIO pin 23
* Green LED on GPIO pin 17
* Red LED on GPIO pin 4
* [Mono USB-powered speaker](http://www.amazon.com/X-Mini-XAM4-B-Portable-Capsule-Speaker/dp/B001UEBN42/ref=sr_1_2?ie=UTF8&qid=1419634849&sr=8-2&keywords=mono+speaker)

## Instructions

**Note: These are *very* loose instructions to help get you started. This guide won't cover the basics of electronic wiring, and Raspbian (the Raspberry Pi flavored Linux distro)**

1. Install [Raspbian Wheezy](http://www.raspberrypi.org/help/noobs-setup/) – I recommend using NOOBS (linked) because it's easier.
2. Use the `raspi-config` menu to change the default password and set your time zone. **Don't skip this step.**
3. Once at the command prompt, run `apt get update` and `apt-get upgrade` to update your base system.
4. Run `apt-get install git`
5. Clone the repo `git clone git@github.com:OutrageousLabs/doorpi.git`
6. `sudo mv rc.local /etc/rc.local` – this overwrites the default rc.local with one that runs the required scripts on boot.
8. Try running `sudo python chime.py` – it should return the following:

  ```
 listening…
  _
  ```

  If so, the Chime script is now running and listening for the reed switch to activate. When the door opens, it will play a sound from the speaker and light the green LED. When the door is closed, it will return back to the red LED.

9. Restart your Pi `sudo shutdown -r now`
10. When the Pi reboots, it will automatically start the network monitor (which will auto-reconnect WiFi if disconnected) and the `chime.py` script.
