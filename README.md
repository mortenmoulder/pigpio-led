# pigpio-led
Changes color of LED strip using a Raspberry Pi and pigpio

## Usage
There are currently 2 different states:

### Change color of all LEDs

    color.py FF0000

This changes the color of all the LEDs to red (#FF0000 is red). Specify a HEX color as the first parameter, and it will simply change the color.

### Fade from one color to another

    color.py FF0000 0000FF 1000

This changes the color of all the LEDs from red (#FF0000) to blue (#0000FF) with a 1000ms fade. 

## Setup
The LEDs are set to run on pin 17, 22, and 24. I followed this guide to set it all up: http://popoklopsi.github.io/RaspberryPi-LedStrip/

I recommend you also follow that guide, otherwise you might end up with a different result than me.

## Installation guide
### 1) Install Python
    sudo apt-get install python
    
### 2) Install pigpio
    rm pigpio.zip
    sudo rm -rf PIGPIO
    wget abyz.co.uk/rpi/pigpio/pigpio.zip
    unzip pigpio.zip
    cd PIGPIO
    make -j4
    sudo make install
    
[Credits to http://abyz.co.uk/rpi/pigpio/download.html](http://abyz.co.uk/rpi/pigpio/download.html)

### 3) Download color.py
    wget https://raw.githubusercontent.com/mortenmoulder/pigpio-led/master/color.py
    
### 4) Run color.py with any of the commands above
    python color.py FF0000
