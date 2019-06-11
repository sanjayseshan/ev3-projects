# Echo server program
import time
import os
import socket
import threading
import struct
import evdev
import sys
from time import sleep

device = evdev.InputDevice('/dev/input/event0')
print(device)



locations = {"none": (0,0), "black": (0,0), "blue" : (0,3),"green": (0,0),"yellow": (4,1),"red": (0,0),"white": (0,0), "brown": (0,0)}
set = [0]*6
scores = {"red":0, "green":0, "pacman":0}
tile_addr = ["10.42.0.1", "10.42.1.1", "10.42.2.1", "10.42.3.1", "10.42.4.1", "10.42.5.1"]
loc = 'green:(0,0)'

enToEs = {"bkg-en.png":"bkg-es.png", "Game Over":"Partido Completado", "Pacman Wins":"Pacman Gana", "Red Ghost Wins":"Fantasma Rojo Gana","Green Ghost Wins":"Fantasma Verde Gana"}


ghostmax = 3 # winnning score for individual ghost
pacmax = 16 # winning score for pacman

connections = []

pacold = 0
redold = 0
blueold = 0

reset = 0
need_reset = 0

def broadcast(data):
        for (s, id) in connections:
           send_str = str(str(data)).encode()
           send_msg = struct.pack('!I', len(send_str))
           send_msg += send_str
           print("sending " + str(len(send_str)) + " bytes")
           print("sending total " + str(len(send_msg)) + " bytes")
           print("sending " + str(send_msg))
           try:
                   s.sendall(send_msg)
                   print("SENDING COMPLETE")
                   #      data = s.recv(1024)
           except Exception as e:
                   print("FAILURE TO SEND.." + str(e.args) + "..RECONNECTING")
                   try:
                           print("sending " + send_msg)
                           s.sendall(send_msg)
                           #         data = s.recv(1024)
                   except:
                           print("FAILED.....Giving up :-( - pass;")
                           pass

def updatedata(caller):
        global pacold,redold,blueold,need_reset
        print "Called by " + caller
	print "Locations: " + str(locations)
	print "Pacman: " + str(scores["pacman"])
	print "Red: " + str(scores["red"])
	print "Green: " + str(scores["green"])
        print "Connected:"
#        print connections
        for (s, id) in connections:
                print id
        print "\n"
        yr,xr = locations['red']
        yr = 5-yr
        yy,xy = locations['yellow']
        yy = 5-yy
        yb,xb = locations['blue']
        yb = 5-yb

#        if need_reset:
#                return
        red = str(scores["red"])
        pac = str(scores["pacman"])
        blue = str(scores["green"])
        
        if int(pac) > int(pacold):
	        os.system('echo seshan | sudo -S aplay pacman_chomp.wav &')
        if int(red) > int(redold):
	        os.system('echo seshan | sudo -S aplay pacman_death.wav &')
        if int(blue) > int(blueold):
	        os.system('echo seshan | sudo -S aplay pacman_death.wav &')

        os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+red+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd1.png')
        os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+blue+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd2.png')
        os.system('convert -background black -fill white -size 16x16 -font Helvetica -pointsize 15 -gravity center label:"'+pac+'" -threshold 50 -morphology Thinning:-1 "LineEnds:-1;Peaks:1.5" -depth 1 cmd3.png')

        if caller == "Reset1":
                #os.system('cp cmd.png cmdtmp.png ; convert cmdtmp.png -fill none -stroke blue -strokewidth 3 -draw "rectangle 77,70 124,90" cmd.png')
                os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \''+bkgPic+'\'" -fill red -draw "image over  '+str(int(xr)*16)+','+str(int(yr)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xy)*16)+','+str(int(yy)*16)+' 0,0 \'pacman.png\'"  -draw "image over  100,18 0,0 \'cmd1.png\'" -draw "image over  100,34 0,0 \'cmd2.png\'" -draw "image over  100,50 0,0 \'cmd3.png\'" -draw "rectangle 0,31 63,95" -fill none -stroke blue -strokewidth 3 -draw "rectangle 77,70 124,90" -fill black -draw "image over '+str(touchx/5)+','+str(touchy/5)+' 0,0 mouse2.png"  cmd.png ')
        if caller == "Exit":
                #os.system('cp cmd.png cmdtmp.png ; convert cmdtmp.png -fill none -stroke blue -strokewidth 3 -draw "rectangle 77,70 124,90" cmd.png')
                os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \''+bkgPic+'\'" -fill red -draw "image over  '+str(int(xr)*16)+','+str(int(yr)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xy)*16)+','+str(int(yy)*16)+' 0,0 \'pacman.png\'"  -draw "image over  100,18 0,0 \'cmd1.png\'" -draw "image over  100,34 0,0 \'cmd2.png\'" -draw "image over  100,50 0,0 \'cmd3.png\'" -draw "rectangle 0,31 63,95" -fill none -stroke blue -strokewidth 3 -draw "rectangle 13,0 159,143" -fill black -draw "image over '+str(touchx/5)+','+str(touchy/5)+' 0,0 mouse2.png"  cmd.png ')
        elif caller == "Language":
                os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \''+bkgPic+'\'" -fill red -draw "image over  '+str(int(xr)*16)+','+str(int(yr)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xy)*16)+','+str(int(yy)*16)+' 0,0 \'pacman.png\'"  -draw "image over  100,18 0,0 \'cmd1.png\'" -draw "image over  100,34 0,0 \'cmd2.png\'" -draw "image over  100,50 0,0 \'cmd3.png\'" -draw "rectangle 0,31 63,95" -fill black -draw "image over '+str(touchx/5)+','+str(touchy/5)+' 0,0 mouse2.png"  cmd.png ')
        else:
                os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \''+bkgPic+'\'" -fill red -draw "image over  '+str(int(xr)*16)+','+str(int(yr)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xy)*16)+','+str(int(yy)*16)+' 0,0 \'pacman.png\'"  -draw "image over  100,18 0,0 \'cmd1.png\'" -draw "image over  100,34 0,0 \'cmd2.png\'" -draw "image over  100,50 0,0 \'cmd3.png\' -fill black -draw "image over '+str(touchx/5)+','+str(touchy/5)+' 0,0 mouse1.png"  cmd.png ')
        
        if int(red) >= ghostmax or int(blue) >= ghostmax or int(pac) >= pacmax:
	        print "GAME OVER"
                need_reset = 1
                if caller != "Language" and caller != "Reset1" and caller != "Touch" and caller != "spinner" and caller != "Exit":
	                os.system('echo seshan | sudo -S aplay pacman-intro.wav &')
	        os.system('cp cmd.png cmdtmp.png')
	        if int(red) >= ghostmax :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \''+gameOver+'\n'+redWon+'\' " cmd.png')
	        if int(blue) >= ghostmax :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \''+gameOver+'\n'+blueWon+'\' " cmd.png')
	        if int(pac) >= pacmax :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \''+gameOver+'\n'+pacWon+'\' " cmd.png')

#                os.system('echo seshan | sudo -S killall fbi')

#                os.system('echo seshan | sudo -S fbi -d /dev/fb0 -T 3 -noverbose -a cmd.png &')

#                for event in device.read_loop():
#                        if event.type == evdev.ecodes.EV_KEY:
#                                print(evdev.categorize(event))
#                                break

                
#                if int(red) >= ghostmax and int(red) > int(redold):
#                        broadcast("RESET")
#	        if int(blue) >= ghostmax and int(blue) > int(blueold):
#                        broadcast("RESET")
#
#	        if int(pac) >= pacmax and int(pac) > int(pacold): #TESTING AS 1 NOT 24
#                        broadcast("RESET")

                
        os.system('echo seshan | sudo -S killall fbi')

        os.system('echo seshan | sudo -S fbi -d /dev/fb0 -T 3 -noverbose -a cmd.png > /dev/null 2>&1 &')
        pacold = pac
        redold = red
        blueold = blue


class Reset(object):
   global reset
   def __init__(self):
           print ("READING INPUT")

   def watch(self):
           global reset,need_reset,locations
           btn_pressed = 0
           btn_processed = 0
           x = -1
           y = -1
           x_p = 0
           y_p = 0

           for event in device.read_loop():
                   #    print(evdev.categorize(event))
                if event.type == evdev.ecodes.EV_KEY:
                           if event.code == evdev.ecodes.BTN_TOUCH:
                                   if btn_pressed == 1:
                                           btn_pressed = 0
                                           btn_processed = 0
                                           print("RELEASED")
                                   else:
                                           btn_pressed = 1
                                           print("PRESSED")
                    
                if event.type == evdev.ecodes.EV_ABS:
                        if event.code == evdev.ecodes.ABS_MT_POSITION_X:
                                #            print("X: " + str(event.value))
                                x = event.value
                                if btn_pressed == 1:
                                        x_p = 1
                        if event.code == evdev.ecodes.ABS_MT_POSITION_Y:
                                #            print("Y: " + str(event.value))            
                                y = event.value
                                if btn_pressed == 1:
                                        y_p = 1

                        if x != -1 and y != -1 and btn_processed == 0:
                                btn_processed = 1
                                print("X: " + str(x))
                                print("Y: " + str(y))
                                if x > 390 and x < 620 and y > 360 and y < 450:
                                        print "Reset Pressed"
                                        reset = 1
                                        updatedata("Reset1")
                                        broadcast("RESET")
	                                os.system('echo seshan | sudo -S aplay win.wav &')
                                        reset = 0
                                        sleep(8)
                                        need_reset = 0
                                        print "Reset Done"
                                        updatedata("Reset")
                                elif x > 710 and x < 800 and y > 410 and y < 480:
                                        print("SWITCHING TO ENGLISH")
                                        bkgPic = "bkg-en.png"
                                        gameOver = "Game Over"
                                        pacWon = "Pacman Wins"
                                        redWon = "Red Ghost Wins"
                                        blueWon = "Green Ghost Wins"
                                        updatedata("Language")
                                elif x > 710 and x < 800 and y > 330 and y < 410:
                                        print("SWITCHING TO SPANISH")
                                        bkgPic = enToEs["bkg-en.png"]
                                        gameOver = enToEs["Game Over"]
                                        pacWon = enToEs["Pacman Wins"]
                                        redWon = enToEs["Red Ghost Wins"]
                                        blueWon = enToEs["Green Ghost Wins"]
                                        updatedata("Language")
                                elif x > 720 and x < 800 and y > 0 and y < 65:
                                        print("Ending PACMAN")
                                        updatedata("Exit")
                                        os.system('echo seshan | sudo -S killall fbi ; sudo service lightdm restart')
                                        sys.exit()
                                else:
                                        updatedata("Touch")

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
	print "Active on port: " + str(port)
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, addresstup = self.sock.accept()
#            conn.settimeout(60)
	    address, tmp = addresstup
#            print "addr: " + str(address)
            if self.port == 5000:
                threading.Thread(target = self.handleTile,args = (conn,address)).start()
            else:
                threading.Thread(target = self.handleGhost,args = (conn,address)).start()

    def handleTile(self, client, address):
        global connections, set
#        print "HANDLE TILE"
        size = 1024
        id = int(address.split(".")[2])
        connections.append((client, "T"+ str(id)))
        updatedata("T" + str(id))
        while True:
            try:
                data = ''
#                print " receiving " + str(struct.calcsize("!I")) + " bytes"
                data_len_str= client.recv( struct.calcsize("!I") )
#                print " received " + str(len(data_len_str)) + " bytes"
                data_len = (struct.unpack("!I", data_len_str))[0]
                while (data_len > 0):
                    data += client.recv( data_len )
                    data_len -= len(data)
		print data + " " + address + " Tile"
                if data:
                    score = data.split(';')[0]
                    set[id] = int(score)
                    loc = data.split(';')[1]
                    color = loc.split(':')[0]
                    coord = loc.split(':')[1].split('\n')[0]
                    locations[color] = eval(coord)
                    scores["pacman"] = sum(set)
		    updatedata("T" + str(id))
#                    print str(locations) + ";" + str(scores["pacman"]) + ";" + str(scores["red"]) + ";" + str(scores["green"])
                else:
                    raise error('Tile disconnected')
            except Exception as e:
                print "TileHandler Exception"
                print str(e.args)
		client.close()
                connections = [i for i in connections if i[0] != client]
                #filter(connections, lambda conn: conn[0] != client)
#                connections.remove((client, "tile "+ str(id)))
		updatedata("T" + str(id))
                return False


    def handleGhost(self, client, address):
        global connections
        setmsgcolor = 1
        msgcolor = ''
#        print "HANDLE GHOST"
        while True:
            try:
                data = ''
                data_len_str= client.recv( struct.calcsize("!I") )
                data_len = (struct.unpack("!I", data_len_str))[0]
                while (data_len > 0):
                    data += client.recv( data_len )
                    data_len -= len(data)
		print data 
                if data:
                    botid = data.split(';')[0]
                    score = data.split(';')[1]
                    if botid == '192.168.0.4':
                      msgcolor = "red"
                    elif botid == '192.168.0.6' or botid == '192.168.0.7':
                      msgcolor = "green"
                    if setmsgcolor:
                            setmsgcolor = 0
                            connections.append((client, "G"+msgcolor))
                    scores[msgcolor] = int(score)
#                   print str(locations) + ";" + str(scores["pacman"]) + ";" + str(scores["red"]) + ";" + str(scores["green"])
		    updatedata("G"+msgcolor)
                else:
                    raise error('Tile disconnected')
            except Exception as e:
                print "GhostHandler Exception"
                print str(e.args)
                if setmsgcolor == 0:
                        connections = [i for i in connections if i[0] != client]
                        #filter(connections, lambda conn: conn[0] != client)
#                        connections.remove((client, self.botcolor + " ghost"))
                client.close()
		updatedata("G"+msgcolor)
                return False


#            except:
#                #client.close()
#                return False

updatedata("main")
os.system('echo seshan | sudo -S aplay pacman-intro.wav &')
Resetter = Reset()
threading.Thread(target = Resetter.watch).start()
        
if __name__ == "__main__":
    tileServer = ThreadedServer('',5000)
    threading.Thread(target = tileServer.listen).start()
    ThreadedServer('',6000).listen()


