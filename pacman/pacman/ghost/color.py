import time,os,socket,struct
import ev3dev.ev3 as ev3

cs1 = ev3.ColorSensor(address='ev3-ports:in4')
cs2 = ev3.ColorSensor(address='ev3-ports:in1')

cs1.mode = "COL-COLOR"
cs2.mode = "COL-COLOR"

ip = socket.gethostbyname(socket.gethostname())

score = 0

HOST = '10.42.0.3'    # The remote host
PORT = 6000             # The same port as used by the server

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
try: 
   s.connect((HOST, PORT))
except Exception as e:
   print("server not available" + str(e.args))
   pass


def sendscore(value):
   send_str = str(ip + ";" + str(value)).encode()
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
          s.connect((HOST, PORT))
          print("sending " + send_msg)
          s.sendall(send_msg)
#         data = s.recv(1024)
      except:
          pass

sendscore(0)

class ControlChannel(object):
   global s,score
   def __init__(self):
      print ("Active on port: 5000 & 6000")

   def watch(self):
      global s, score
      while True:
         data = ''
         try: 
            data_len_str= s.recv( struct.calcsize("!I") )
            data_len = (struct.unpack("!I", data_len_str))[0]
            while (data_len > 0):
               data += s.recv( data_len ).decode()
               data_len -= len(data)
            print(data)
            control(data)
         except Exception as e:
            print("FAILURE TO RECV.." + str(e.args) + "..RECONNECTING")
            try:
               s.close()
               s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
               s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
               s.connect((HOST, PORT))
            except:
               pass
           # threading.Thread(target = self.control,args = (str(msg))).start()

   def control(self, data):
       global s, score
       time.sleep(1)
       print(data)
       if "RESET" in data:
          print("resetting")
          score = 0
          
Server = ControlChannel('',6000)
threading.Thread(target = Server.watch).start()


while True:
 try:
     if cs1.value() == 4:
           print("PACMAN CAUGHT")
           score = score+1
           sendscore(score)
           os.system('beep -f 300 -l 1000')
     if cs2.value() == 4:
           print("PACMAN CAUGHT")
           score = score+1
           sendscore(score)
           os.system('beep -f 300 -l 1000')
     if cs1.value() != 0 or cs2.value() != 0:
           print(cs1.value())
           print(cs2.value())
 except:
     pass
