import sys, time, os
import time

import socket

#s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#s.connect(("10.42.0.3", 1234))
    #s.sendall(content)
    #s.shutdown(socket.SHUT_WR)
    #while 1:
    #    data = s.recv(1024)
    #    if data == "":
    #        break
    #    print "Received:", repr(data)
    #print "Connection closed."
    #s.close()


locations = {"none": "(0, 0)", "black": "(0, 0)", "blue" : "(0, 0)","green": "(0, 0)","yellow": "(0, 0)","red": "(0, 0)","white": "(0, 0)", "brown": "(0, 0)"}
#file = open("locations.txt","w")


#    logfile = open("colors","r")
#    loglines = follow(logfile)
#    for line in loglines:
#        print line,
pacold = 0
redold = 0
grnold = 0
while 1:
#    print "hi"
    try:
#	print "a"
        line = sys.stdin.readline()
#	print "b"
    except KeyboardInterrupt:
        break

    if not line:
	fdsf=0
#        break
#	print "CONT"
    print line
    if "blue" in line:    
     data = line.split('\n')[0].split(";") # = [locations, pmscore, redghost, greenghost]
     locations = eval(data[0])
     print locations
     print locations['red']
     y,x = locations['red']
     print x 
     print y
     print locations['yellow']
     ya,xa = locations['yellow']
     print xa
     print ya
     print locations['blue']
     yb,xb = locations['blue']
     print xb
     print yb
     red = data[2]
     pac = data[1]
     blue = data[3]
     if int(pac) > int(pacold):
	os.system('aplay pacman_chomp.wav &')
     if int(red) > int(redold):
	os.system('aplay pacman_death.wav &')
     if int(blue) > int(grnold):
	os.system('aplay pacman_death.wav &')

     os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+red+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd1.png')
     os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+blue+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd2.png')
     os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+pac+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd3.png')
     os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \'pacman-base.png\'" -fill red -draw "image over  '+str(int(x)*16)+','+str(int(y)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xa)*16)+','+str(int(ya)*16)+' 0,0 \'pacman.png\'"  -draw "image over  86,18 0,0 \'cmd1.png\'" -draw "image over  86,34 0,0 \'cmd2.png\'" -draw "image over  86,50 0,0 \'cmd3.png\'" cmd.png ')
     if int(red) >= 3 or int(blue) >= 3 or int(pac) >= 24:
	print "GAME OVER"
	os.system('cp cmd.png cmdtmp.png')
	os.system('aplay pacman_intermission.wav &')
	if int(red) >= 3 :
		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nRED GHOST WON\' " cmd.png')
	if int(blue) >= 3 :
		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nBLUE GHOST WON\' " cmd.png')
	if int(pac) >= 24 :
		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nPACMAN WON\' " cmd.png')

	if int(red) >= 3 and int(red) > int(redold):
#		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nRED GHOST WON\' " cmd.png')
		os.system('sshpass -p maker ssh robot@10.42.0.3 "echo reset ; ~/reset.sh" &')
	if int(blue) >= 3 and int(blue) > int(grnold):
#		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nBLUE GHOST WON\' " cmd.png')
		os.system('sshpass -p maker ssh robot@10.42.0.3 "echo reset ; ~/reset.sh" &')
	if int(pac) >= 24 and int(pac) > int(pacold):
#		os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nPACMAN WON\' " cmd.png')
		os.system('sshpass -p maker ssh robot@10.42.0.3 "echo reset ; ~/reset.sh" &')
        #os.system('killall fbi ; fbi -d /dev/fb0 -T 3 -noverbose -a cmd.png &')
     os.system('killall fbi')
#     os.system('cat /dev/zero > /dev/fb0')
     os.system('fbi -d /dev/fb0 -T 3 -noverbose -a cmd.png &')
     pacold = pac
     redold = red
     grnold = blue
