#import ev3dev.ev3 as ev3
#Name your gcode file file.gcode
#GCODE to SanjayCODE v1.3 converter v1.2
#run the code and output to rtf (python GCODE-TO-SanjayCODE-RTF-EV3.py > gcode.rtf)
# the rtf is now in SanjayCODE (R) and you can upload it to the EV3 "master" project
# SanjayCODE v1.3 format: 
#X coord
#Y coord
#Z coord
#Extruder 1/0 (On/Off)
#100000X,Y,Z = done with print
import time,sys
file_name = "file.gcode"  # put your filename here
zdpm = 1296/150
xdpm = (2378/170)
ydpm = (-1733/190)
laste=0
lastx=0
lasty=0
lastz=0
lastf=0
ex = 1
with open(file_name, 'r+') as f:
    coordinates = []
    content = f.readlines()
    for line in content:
        if ';' in line:
            try:
                gcode, comment = line.strip('\n').split(";")
            except:
                print(' ERROR 1: \n', line, '\n')
        elif '(' in line:
            try:
                gcode, comment = line.strip('\n').strip(')').split("(")
            except:
                print('ERROR 2: \n', line, '\n')
        else:
            gcode = line.strip('\n')
            comment = ""

        coordinate_set = {}
        if 'retract' not in comment and 'layer' not in comment and gcode:
            for num in gcode.split()[1:]:
                if len(num) > 1:
                    try:
                        coordinate_set[num[:1]] = float(num[1:])
                    except:
                        print('ERROR 3: \n', gcode, '\n')
            coordinates.append(coordinate_set)
#for coord in coordinates:
            coord = coordinate_set
            if 'S' in coord or coord == {}:
            	coord = coordinate_set
            else:
#            	print(coord)
            	if 'X' in coord:
                    x = coord['X']
            	else:
                    x = 0
            	if 'Y' in coord:
                    y = coord['Y']
            	else:
                    y = 0
            	if 'Z' in coord:
                    z = coord['Z']
            	else:
                    z = 0
                if 'E' in coord:
                    e = coord['E']
                else:
                    e = 0
                if 'F' in coord:
                        f = coord['F']
                else:
                        f = 0

#		print e
                if e != -100:
#			print str(e) + "  " + str(laste)
#			print e
			if e <= laste or e == 0:
				ex = 0
#				print(str(e)+" "+str(laste))
			else:
				ex = 1
			laste = e
		else:
			ex = 1
#		print "X,Y,Z,E"
#		if x == 0 and y == 0:
#			xxxxx=0
#		else:
		if z == 0:
#			print "H"
			z = lastz
		else:
			lastz = z
		if f == 0:
#			print "H"
			f = lastf
		else:
			lastf = f
		if y != 0:
			lasty = y
		else:
			y = lasty
		if x != 0:
			lastx = x
		else:
			x = lastx
		ex = str(ex)
		x = str(x)
		y = str(y)
		z = str(z)
		f = str(f)

#		sys.stderr.write("XYZEF")
#		sys.stdout.write("XYZEF")
#                sys.stdout.write('\r')
#                sys.stderr.write('\n\r')
		sys.stderr.write(x)
		sys.stdout.write(x)
                sys.stdout.write('\r')
                sys.stderr.write('\n\r')
		sys.stderr.write(y)
		sys.stdout.write(y)
                sys.stdout.write('\r')
                sys.stderr.write('\n\r')
		sys.stderr.write(z)
		sys.stdout.write(z)
                sys.stdout.write('\r')
                sys.stderr.write('\n\r')
		sys.stderr.write(ex)
		sys.stdout.write(ex)
                sys.stdout.write('\r')
                sys.stderr.write('\n\r')
		sys.stderr.write(f)
		sys.stdout.write(f)
                sys.stdout.write('\r')
                sys.stderr.write('\n\r')
#            	if z != 0:
#                    movecoordxyz(x,y,z)
#            	else:
#                    movecoordxy(x,y)
#
#        time.sleep(1.3)


sys.stderr.write('100000')
sys.stdout.write('100000')
sys.stdout.write('\r')
sys.stderr.write('\n\r')
sys.stderr.write('100000')
sys.stdout.write('100000')
sys.stdout.write('\r')
sys.stderr.write('\n\r')
sys.stderr.write('100000')
sys.stdout.write('100000')
sys.stdout.write('\r')
sys.stderr.write('\n\r')
