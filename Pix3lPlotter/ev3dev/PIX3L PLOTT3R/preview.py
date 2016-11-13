#!/usr/bin/python
# -*- coding: utf-8 -*- import python packages

#install --> (sudo) apt-get install python-pip --> (sudo) pip install pillow python-ev3dev
#running --> run (sudo) python pythonfilename.py imagefilename.png (jpg will work along with others types) -->
#            you will be given a dialogue --> just type "" and return/enter to continue

from PIL import Image, ImageFilter
import ev3dev.ev3 as ev3
import time
from ev3dev import *
import os
import sys

# paper resolution
horiz_deg = 1950; #degress max move
horiz_width = 6; #inches
horiz_res = horiz_deg/horiz_width-10; # degrees per inch
vertical_deg = -17000; #degress max move
vertical_width = 6.5; #inches
vertical_res = vertical_deg/vertical_width; # degrees per inch
vert_move = 120;
horiz_move = vert_move*horiz_res/vertical_res;
res = (horiz_deg*-1/horiz_move);

#function to ensure the motor has stopped before moving on


#resize and flip image
filename = sys.argv[1]
cmd = "convert " + filename + " -flop -resize " + str(res) +" -monochrome print.jpg"
os.system(cmd) #execute command

cmd = "convert "+filename+" -rotate 90 -trim -flatten -flop -resize 178x128 -monochrome ev3screen.jpg"

#cmd = "convert " + filename + " -threshold 90% -flop -resize " + str(res) +" /home/robot/print.jpg"
os.system(cmd) #execute command
image_file = Image.open('print.jpg') # open image print.jpg in current directory
image_file = image_file.convert('1') # convert image to pure black and white (just in case image is greyscale or color)
image_file.save('print.png') # save b&w image

w = 0
h = 0
l = 0
img = Image.open('print.png') #open black and white image
width, height = img.size # get image size
array = []
print width," x ", height
while h != height:
        while w != width:
                array.append(img.getpixel((w, h))) #get black or white of each pixel
                w = w+1 #move to next pixel
        w = 0 #reset width counter
        h = h+1 #move to next row

all_pixels = array #save array of pixels to all_pixels

x = input('Type text to preview picture (in quotes) >>') #wait until dialogue is answered then show preview
os.system('service brickman stop')

filename = sys.argv[1]
#cmd = "convert " + filename + " -threshold 90% -flop -resize " + str(res) +" -flatten /home/robot/print.jpg"
#cmd = "convert "+ filename +" -flatten -flop -resize 83 +dither -colors 2 -colorspace gray -normalize -negate print.jpg"


width, height = img.size #get image size
xd = 0
yd = 0
xda = 0
while yd != height:
    while xd != width:
        if all_pixels[xda] == 0: #is pixel black?
            print "█", #print block if black pixel
        else:
            print " ",
        xd = xd + 1
        xda = xda + 1
    print(" ")
    yd = yd + 1
    xd = 0

img2 = Image.open("ev3screen.jpg")
raw = img2.tobytes()
image = Image.frombytes(img2.mode, img2.size, raw)
lcd = ev3.Screen()
lcd._img.paste(image, (0, 0))
lcd.update()

x = input('Is this picture ok? If not pres ctrl-c >>') #wait for dialogue to be answered then start printing
os.system('service brickman start')
