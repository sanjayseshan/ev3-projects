#!/usr/bin/python3

# Echo client program
import socket,time
import ev3dev.ev3 as ev3
from time import sleep


ult1 = ev3.UltrasonicSensor(address='ev3-ports:in1')
ult2 = ev3.UltrasonicSensor(address='ev3-ports:in2')
ult3 = ev3.UltrasonicSensor(address='ev3-ports:in3')
ult4 = ev3.UltrasonicSensor(address='ev3-ports:in4')

HOST = "192.168.0." + str(int(socket.gethostbyname(socket.gethostname()).split('.')[3])-1)    # The remote host
PORT = 50007              # The same port as used by the server

def sendcmd(direction,socket):
       socket.sendall(dir.encode())
       
print("INIT")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
try:
       s.connect((HOST, PORT))
       print("connected to " + HOST)
except:
       pass
while True:
       try:
              while True:
                     if ult1.value() < 70:
                            dir = "F"
                            sendcmd(dir,s)
                            while ult1.value() < 70:
                                   continue
                     elif ult2.value() < 70:
                            dir = "R"
                            sendcmd(dir,s)
                            while ult2.value() < 70:
                                   continue
                     elif ult3.value() < 70:
                            dir = "B"
                            sendcmd(dir,s)
                            while ult3.value() < 70:
                                   continue
                     elif ult4.value() < 70:
                            dir = "L"
                            sendcmd(dir,s)
                            while ult4.value() < 70:
                                   continue
                     else:
                            dir = "S"
                            sendcmd(dir,s)
                            while ult1.value() > 70 and ult2.value() > 70 and ult3.value() > 70 and ult4.value() > 70:
                                   continue
                     print(dir)
       except Exception as e:
              print("FAILURE TO SEND.." + str(e.args) + "..RECONNECTING") 
              try:
                     s.close()
                     s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                     s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
                     s.connect((HOST, PORT))
                     print("connected to " + HOST)
              except:
                     sleep(2)
                     pass
 
#       a = str(time.time())
#       print("SENT")
#       data = s.recv(1024)
#       print('Received', float(eval(repr(data))))
#       a = str(time.time())
#       print((float(a) - float(eval(repr(data))))/2)
#       print(a)
#       print(float(eval(repr(data))))
#       time.sleep(0.5)
