# Echo server program
import time
import os
import socket
import threading
import struct

locations = {"none": (0,0), "black": (0,0), "blue" : (0,3),"green": (0,0),"yellow": (4,1),"red": (0,0),"white": (0,0), "brown": (0,0)}
set = [0]*6
scores = {"red":0, "green":0, "pacman":0}
tile_addr = ["10.42.0.1", "10.42.1.1", "10.42.2.1", "10.42.3.1", "10.42.4.1", "10.42.5.1"]
loc = 'green:(0,0)'

pacold = 0
redold = 0
blueold = 0

def transmit(data, iplist5000, iplist6000):
        tmp = [iplist5000,iplist6000]
        for list in tmp:
         for ip in list:
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
                           s.connect((ip, str(1000*tmp.index(list)+5000)))
                           print("sending " + send_msg)
                           s.sendall(send_msg)
                           #         data = s.recv(1024)
                   except:
                           print("FAILED.....Giving up :-( - pass;")
                           pass

def updatedata():
        global pacold,redold,blueold
	print "Locations: " + str(locations)
	print "Pacman: " + str(scores["pacman"])
	print "Red: " + str(scores["red"])
	print "Green: " + str(scores["green"])

        y,x = locations['red']
        ya,xa = locations['yellow']
        yb,xb = locations['blue']

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
        os.system('convert -size 160x96 xc:black -fill red -draw "image over  0,0 0,0 \'pacman-base.png\'" -fill red -draw "image over  '+str(int(x)*16)+','+str(int(y)*16)+' 0,0 \'red.png\'" -draw "image over  '+str(int(xb)*16)+','+str(int(yb)*16)+' 0,0 \'green.png\'" -fill yellow -draw "image over  '+str(int(xa)*16)+','+str(int(ya)*16)+' 0,0 \'pacman.png\'"  -draw "image over  86,18 0,0 \'cmd1.png\'" -draw "image over  86,34 0,0 \'cmd2.png\'" -draw "image over  86,50 0,0 \'cmd3.png\'" cmd.png ')
        if int(red) >= 3 or int(blue) >= 3 or int(pac) >= 1:
	        print "GAME OVER"
	        os.system('cp cmd.png cmdtmp.png')
	        os.system('echo seshan | sudo -S aplay pacman_intermission.wav &')
	        if int(red) >= 3 :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nRED GHOST WON\' " cmd.png')
	        if int(blue) >= 3 :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nBLUE GHOST WON\' " cmd.png')
	        if int(pac) >= 24 :
		        os.system('convert cmdtmp.png -font Helvetica -weight 700  -pointsize 15 -undercolor white -draw "gravity center fill blue text 0,0 \'GAME OVER\nPACMAN WON\' " cmd.png')

	        if int(red) >= 3 and int(red) > int(redold):
                        transmit("RESET",tile_addr,["192.168.0.4","192.168.0.6"])
	        if int(blue) >= 3 and int(blue) > int(blueold):
                        transmit("RESET",tile_addr,["192.168.0.4","192.168.0.6"])

	        if int(pac) >= 1 and int(pac) > int(pacold): #TESTING AS 1 NOT 24
                        transmit("RESET",tile_addr,["192.168.0.4","192.168.0.6"])

        
        os.system('echo seshan | sudo -S killall fbi')

        os.system('echo seshan | sudo -S fbi -d /dev/fb0 -T 3 -noverbose -a cmd.png &')
        pacold = pac
        redold = red
        blueold = blue


updatedata()

        
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
#        print "HANDLE TILE"
        size = 1024
        id = int(address.split(".")[2])
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
		    updatedata()
#                    print str(locations) + ";" + str(scores["pacman"]) + ";" + str(scores["red"]) + ";" + str(scores["green"])
                else:
                    raise error('Tile disconnected')
            except Exception as e:
                print "TileHandler Exception"
                print str(e.args)
		client.close()
                return False


    def handleGhost(self, client, address):
        size = 1024
#        print "HANDLE GHOST"
        while True:
            try:
                data = ''
#                print " receiving " + str(struct.calcsize("!I")) + " bytes"
                data_len_str= client.recv( struct.calcsize("!I") )
#                print " received " + str(len(data_len_str)) + " bytes"
                data_len = (struct.unpack("!I", data_len_str))[0]
#                print " receiving " + str(data_len) + " bytes"
                while (data_len > 0):
                    data += client.recv( data_len )
                    data_len -= len(data)
#                    print " receiving " + str(data_len) + " more bytes"
		print data + " " + address + " Ghost"
                if data:
                    botid = data.split(';')[0]
                    score = data.split(';')[1]
#                    print("addr_bot: "+botid)
                    if botid == '192.168.0.4':
                      scores["red"] = int(score)
                    if botid == '192.168.0.6':
                      scores["green"] = int(score)
#                    print str(locations) + ";" + str(scores["pacman"]) + ";" + str(scores["red"]) + ";" + str(scores["green"])
		    updatedata()
                else:
                    raise error('Tile disconnected')
            except Exception as e:
                print "TileHandler Exception"
                print str(e.args)
                client.close()
                return False


#            except:
#                #client.close()
#                return False

if __name__ == "__main__":
    tileServer = ThreadedServer('',5000)
    threading.Thread(target = tileServer.listen).start()
    ThreadedServer('',6000).listen()


