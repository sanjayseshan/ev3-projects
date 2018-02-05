#!/usr/bin/python3

# Echo server program
import socket,time,os,struct,threading
import ev3dev.ev3 as ev3
from time import sleep

B = ev3.LargeMotor('outB')
C = ev3.LargeMotor('outC')

cs1 = ev3.ColorSensor(address='ev3-ports:in4')
cs2 = ev3.ColorSensor(address='ev3-ports:in1')

cs1.mode = "COL-COLOR"
cs2.mode = "COL-COLOR"

ip = socket.gethostbyname(socket.gethostname())
cc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cc_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)

score = 0


print("INIT")

class Move(object):
    def __init__(self):
        self.host = ''                 # Symbolic name meaning all available interfaces
        self.port = 50007              # Arbitrary non-privileged port
        self.active = 1
        print("MOVE INIT")

    def drive(self):
        move_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        move_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        move_sock.bind((self.host, self.port))
        move_sock.listen(1)
        while True:
            try:
                conn, addr = move_sock.accept()
                ip,port = addr

                with conn:
                    print('Connection from', addr)
                    while True:
                        data = conn.recv(1)
                        print(data)
                        if not data:
                            conn.close()
                            break
                        if self.active:
                            dir = data.decode()
                            if dir == "F":
                                B.run_forever(speed_sp=250)
                                C.run_forever(speed_sp=250)
                            elif dir == "B":
                                B.run_forever(speed_sp=-250)
                                C.run_forever(speed_sp=-250)
                            elif dir == "L":
                                B.run_forever(speed_sp=200)
                                C.run_forever(speed_sp=-200)
                            elif dir == "R":
                                B.run_forever(speed_sp=-200)
                                C.run_forever(speed_sp=200)
                            elif dir == "S":
                                B.stop()
                                C.stop()
                        else:
                            B.stop()
                            C.stop()                             
            except:
                conn.close


                        
class ControlChannel(object):
   global cc_sock,score
   def __init__(self):
       self.host = '10.42.0.3'    # The remote host
       self.port = 6000             # The same port as used by the server
       print ("Active on port: 6000")

   def control(self, data):
       global score
       time.sleep(1)
       print(data)
       if "RESET" in data:
          print("resetting")
          score = 0
          self.sendscore(score)

   def watch(self):
      global cc_sock, score
      cc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
      cc_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
      try:
          cc_sock.connect((self.host, self.port))
          print("Connected! to " + self.host)
      except:
          pass
      while True:
         data = ''
         try: 
            data_len_str= cc_sock.recv( struct.calcsize("!I") )
            data_len = (struct.unpack("!I", data_len_str))[0]
            while (data_len > 0):
               data += cc_sock.recv( data_len ).decode()
               data_len -= len(data)
            print(data)
            self.control(data)
         except Exception as e:
            print("FAILURE TO RECV.." + str(e.args) + "..RECONNECTING")
            try:
               cc_sock.close()
               cc_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               cc_sock.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
               cc_sock.connect((self.host, self.port))
               print("Connected! to " + self.host)
               self.sendscore(score)
            except:
               sleep(2)
               pass
           # threading.Thread(target = self.control,args = (str(msg))).start()

   def sendscore(self,value):
       global cc_sock
       send_str = str(ip + ";" + str(value)).encode()
       send_msg = struct.pack('!I', len(send_str))
       send_msg += send_str
       print("sending " + str(len(send_str)) + " bytes")
       print("sending total " + str(len(send_msg)) + " bytes")
       print("sending " + str(send_msg))
       try:
           cc_sock.sendall(send_msg)
           print("SENDING COMPLETE")
           #      data = s.recv(1024)
       except Exception as e:
           print("FAILURE TO SEND.." + str(e.args) + "..RECONNECTING")
           try:
               cc_sock.connect((self.host, self.port))
               print("connected to " + self.host)
               print("sending " + send_msg)
               cc_sock.sendall(send_msg)
           except:
               sleep(2)
               pass

          
moving = Move()
threading.Thread(target = moving.drive).start()
Server = ControlChannel()
threading.Thread(target = Server.watch).start()
sleep(1)
Server.sendscore(0)
pac_count = 0
while True:
 try:
     if cs1.value() == 4 or cs2.value() == 4:
         pac_count += 1
         sleep(.02)
         print("saw yellow")
         if pac_count > 2:
             moving.active = 0
             print("PACMAN CAUGHT")
             score = score+1
             Server.sendscore(score)
             os.system('beep -f 300 -l 500')
             sleep(3)
             os.system('beep -f 300 -l 500')
             moving.active = 1
             pac_count = 0
     else:
         pac_count = 0
         
#     if cs2.value() == 4:
#           print("PACMAN CAUGHT")
#           score = score+1
#           Server.sendscore(score)
#           os.system('beep -f 300 -l 1000')
#     if cs1.value() != 0 or cs2.value() != 0:
#           print(cs1.value())
#           print(cs2.value())
 except:
     pass
