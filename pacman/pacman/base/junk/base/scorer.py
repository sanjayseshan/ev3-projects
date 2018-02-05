# Echo server program
import time
import os
import socket
import threading

locations = {"none": (0,0), "black": (0,0), "blue" : (0,0),"green": (0,0),"yellow": (0,0),"red": (0,0),"white": (0,0), "brown": (0,0)}
set = [0]*6
scores = {"red":0, "green":0, "pacman":0}

loc = 'green:(0,0)'

class ThreadedServer(object):
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    def listen(self):
        self.sock.listen(5)
        while True:
            conn, address = self.sock.accept()
            conn.settimeout(60)
            if address == ...:
            threading.Thread(target = self.handleTile,args = (conn,address)).start()

    def handleTile(self, client, address):
        size = 1024

        while True:
            try:
                data = client.recv(size)
                if data:
                    # Set the response to echo back the recieved data
                    response = data
                    client.send(response)
                    score = data.split(';')[0]
                    if address== '127.0.0.1' or address== '10.42.0.3' or address== '10.42.1.3' or address== '10.42.2.3' or address== '10.42.3.3' or address== '10.42.4.3' or address== '10.42.5.3' or address== '192.168.0.20':
                      set[0] = int(score)
                      loc = data.split(';')[1]
                    if address== '10.42.1.1':
                      set[1] = int(score)
                      loc = data.split(';')[1]
                    if address== '10.42.2.1':
                      set[2] = int(score)
                      loc = data.split(';')[1]
                    if address== '10.42.3.1':
                      set[3] = int(score)
                      loc = data.split(';')[1]
                    if address== '10.42.4.1':
                      set[4] = int(score)
                      loc = data.split(';')[1]
                    if address== '10.42.5.1':
                      set[5] = int(score)
                      loc = data.split(';')[1]
                    if address== '192.168.0.1':
                      scores["red"] = int(score)
                    if address== '192.168.0.5':
                      scores["green"] = int(score)
                    #  time.sleep(1)
                    # print line
                    color = loc.split(':')[0]
                    coord = loc.split(':')[1].split('\n')[0]
                    locations[color] = eval(coord)
                    # print locations
                    scores["pacman"] = sum(set)
                    print str(locations) + ";" + str(scores["pacman"]) + ";" + str(scores["red"]) + ";" + str(scores["green"])
                else:
                    raise error('Tile disconnected')
            except:
                client.close()
                return False

if __name__ == "__main__":
    ThreadedServer('10.42.0.3',5001).listen()
    ThreadedServer('10.42.1.3',5002).listen()
    ThreadedServer('10.42.2.3',5003).listen()
    ThreadedServer('10.42.3.3',5004).listen()
    ThreadedServer('10.42.4.3',5005).listen()
    ThreadedServer('10.42.5.3',5006).listen()
    ThreadedServer('192.168.0.1',6001).listen()
    ThreadedServer('192.168.0.5',6005).listen()

