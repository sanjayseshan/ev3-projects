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
horiz_res = horiz_deg/horiz_width; # degrees per inch
vertical_deg = 3496; #degress max move
vertical_width = 10; #inches
vertical_res = vertical_deg/vertical_width; # degrees per inch
vert_move = 12;
horiz_move = vert_move*horiz_res/vertical_res;
res = (horiz_deg/horiz_move);
#print res
res = 140
horiz_move = 12;
bottom = -107
#function to ensure the motor has stopped before moving on
xxx = 0
def waitformotor(motor):
    #run more than once to ensure that motor is stopped and that it was not a false reading
#    print motor.state
#    x = motor.state
#    if motor.state != []:
    while motor.state != []:
#	if motor.state != []:
#		x = motor.state
#	else:
#		x = ['done']
        xxx = 0
# define motors and use brake mode

paper = ev3.MediumMotor('outA')
pen = ev3.MediumMotor('outB')
LR = ev3.MediumMotor('outC')
pen.stop_action = "brake"
LR.stop_action = "brake"
paper.stop_action = "brake"
LR.ramp_up_sp=100
LR.ramp_down_sp=200
LR.reset()
#LR.run_to_abs_pos(position_sp=-50, duty_cycle_sp=75)
waitformotor(LR)
waitformotor(LR)
LR.reset()
paper.reset()
#LR.speed_regulation_enabled=u'on'

#move paper until color sensor recieves >50 reading

#paper.speed_regulation_enabled=u'on'
pen.run_timed(time_sp=3000, speed_sp=100)
waitformotor(pen)
pen.reset()
print "pen up"
ts = ev3.TouchSensor()
while ts.value() != 1:
        print ts.value()
        print "Please activate!"

#alternate rel pos make dot 
#uncomment
#pen.run_to_abs_pos(position_sp=bottom-1010, speed_sp=1000, ramp_down_sp=500)
#replace paper in makedot()
#    pen.run_to_rel_pos(position_sp=1010, speed_sp=1100, ramp_down_sp=500)
#    pen.run_to_rel_pos(position_sp=-1010, speed_sp=1100, ramp_down_sp=500)

#make a function to make a dot on the page
def makedot():
#    pen.run_to_abs_pos(position_sp=bottom, speed_sp=1100, ramp_down_sp=500)
    pen.run_timed(time_sp=300, speed_sp=-1000)
    waitformotor(pen)
    waitformotor(pen) #double check if motor is stopped before raising pen
#    pen.run_to_abs_pos(position_sp=0, speed_sp=1000, ramp_down_sp=500)
    pen.run_timed(time_sp=300, speed_sp=1000)
    waitformotor(pen)
    waitformotor(pen)

#resize and flip image
filename = sys.argv[1]
cmd = "convert " + filename + " -flop -rotate 90 -negate -resize " + str(res) +" -monochrome print.jpg"
os.system(cmd) #execute command

cmd = "convert "+filename+" -rotate 90 -trim -flatten -flop -resize 170 -monochrome ev3screen.jpg"

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

#x = input('Type text to preview picture (in quotes) >>') #wait until dialogue is answered then show preview
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

#x = input('Is this picture ok? If not pres ctrl-c >>') #wait for dialogue to be answered then start printing
os.system('service brickman start')
xd = 0
yd = 0
xda = 0
while yd != height:
    while xd != width:
        if all_pixels[xda] == 0: #is pixel black?
            print "█", #print block if black pixel
            # lower and raise pen
 #           pen.run_timed(time_sp=250, duty_cycle_sp=-15)
            LR.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
            waitformotor(LR)
            makedot()
            # move pen left
        else:
            print " ",
            #move pen left
#            LR.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
#            waitformotor(LR)
        xd = xd + 1
        xda = xda + 1

    print(" ")
    yd = yd + 1
#    xd = 0
    # move paper forward
#    paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=300)
    paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
    # reset pen location
#    LR.run_to_abs_pos(position_sp=0, duty_cycle_sp=75)
#    waitformotor(paper)
    waitformotor(paper)
    paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
    # reset pen location
#    LR.run_to_abs_pos(position_sp=0, duty_cycle_sp=75)
#    waitformotor(paper)
    waitformotor(paper)
#    waitformotor(LR)
#    waitformotor(LR)
#    print height-yd
    if yd < height-1:
#      print "in"
      xd = width
      xda = xda+width
      pixels_r2 = []
      xdb = 0
      while xd != 0:
        if all_pixels[xda] == 0: #is pixel black?
            #print "█", #print block if black pixel
	    pixels_r2.append("█")
            # lower and raise pen
#           pen.run_timed(time_sp=250, duty_cycle_sp=-15)
            LR.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
            waitformotor(LR)
            makedot()
            # move pen left
        else:
	    pixels_r2.append(" ")
            #print " ",
            #move pen left
#            LR.run_to_abs_pos(position_sp=horiz_move*xd, speed_sp=400, ramp_down_sp=500)
#            waitformotor(LR)
#	print xd
#	print xda
#	print all_pixels[xda]
        xd = xd - 1
        xda = xda - 1
        xdb = xdb + 1
      for block in pixels_r2:
		print block,
      print(" ")
      xda = xda+width
      xd = 0
      yd = yd+1
      paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
      waitformotor(paper)
      paper.run_to_abs_pos(position_sp=vert_move*(yd), speed_sp=250,ramp_down_sp=500)
      waitformotor(paper)

#paper.run_timed(time_sp=5000, speed_sp=-1000) #eject paper
#time.sleep(5)
#LR.run_timed(time_sp=5000, duty_cycle_sp=75) #eject paper
#LR.run_to_abs_pos(position_sp=0, duty_cycle_sp=75) #reset to original position
#time.sleep(2)
paper.run_to_abs_pos(position_sp=0, speed_sp=1000)

LR.run_to_abs_pos(position_sp=0, speed_sp=1000)
pen.run_to_abs_pos(position_sp=0, speed_sp=1000)
waitformotor(paper)
waitformotor(LR)
waitformotor(pen)

