from __future__ import division
import os
import time
import sys
import struct
import re
import colorsys

def hex2rgb(rgb):
    return struct.unpack('BBB', rgb.decode('hex'))

def color(r, g, b):
    os.system("echo p 17 " + str(r) + " > /dev/pigpio")
    os.system("echo p 22 " + str(g) + " > /dev/pigpio")
    os.system("echo p 24 " + str(b) + " > /dev/pigpio")

def hsv2rgb(h,s,v):
    return tuple(i * 255 for i in colorsys.hsv_to_rgb(h,s,v))

if(len(sys.argv) == 2):
    if bool(re.search("^(?:[0-9a-f]{3}){1,2}$", sys.argv[1], re.IGNORECASE)):
        rgb = hex2rgb(sys.argv[1])
        rgb = re.sub('[\(\) ]', '', str(rgb))
        rgb = rgb.split(",")

        r = rgb[0]
        g = rgb[1]
        b = rgb[2]

        color(r,g,b)

if(len(sys.argv) == 4):
    if bool(re.search("^(?:[0-9a-f]{3}){1,2}$", sys.argv[1], re.IGNORECASE)) and bool(re.search("^(?:[0-9a-f]{3}){1,2}$", sys.argv[2], re.IGNORECASE)) and sys.argv[3].isdigit():
        timeToTake = int(sys.argv[3])
        rgb = hex2rgb(sys.argv[1])
        rgb = re.sub('[\(\) ]', '', str(rgb))
        rgb = rgb.split(",")

        rgb = colorsys.rgb_to_hsv(int(rgb[0])/255, int(rgb[1])/255, int(rgb[2])/255)
        print "rgb: " + str(rgb)

        rgb2 = hex2rgb(sys.argv[2])
        rgb2 = re.sub('[\(\) ]', '', str(rgb2))
        rgb2 = rgb2.split(",")

        rgb2 = colorsys.rgb_to_hsv(int(rgb2[0])/255, int(rgb2[1])/255, int(rgb2[2])/255)
        print "rgb2: " + str(rgb2)

        steps = abs(rgb[0] - rgb2[0]) * 360
        stepsToFall = abs((rgb[0] - rgb2[0])) / steps
        hue = rgb[0]
        timeToSleep = timeToTake / steps / 1000
        print "Time to sleep: " + str(timeToSleep)
        for i in range(0, int(steps)):
            newRgb = hsv2rgb(hue, rgb[1], rgb[2])
            if rgb[0] > rgb2[0]:
                hue = hue - stepsToFall
            else:
                hue = hue + stepsToFall
            color(newRgb[0], newRgb[1], newRgb[2])
            time.sleep(timeToSleep)
