import ev3dev.ev3 as ev3 
import socket
import struct


cs = [ev3.ColorSensor(address='ev3-ports:in1'),ev3.ColorSensor(address='ev3-ports:in2'),ev3.ColorSensor(address='ev3-ports:in3'),ev3.ColorSensor(address='ev3-ports:in4')]
locations = {"none": (0,0), "black": (0,0), "blue" : (0,0),"green": (0,0),"yellow": (0,0),"red": (0,0),"white": (0,0), "brown": (0,0)}
colors = ['none','black','blue','green','yellow','red','white','brown']
colorcount = [[0]*32,[0]*32,[0]*32,[0]*32]
eaten = [0]*4
monitoring = [0]*4
HOST = '10.42.0.3'    # The remote host
PORT = 5000             # The same port as used by the server
idfile = open("id.txt")
setID = int(idfile.readline().split('\n')[0])
pmscore = 0
for n in range(0, 4):
   cs[n].mode='COL-AMBIENT'


s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
try: 
   s.connect((HOST, PORT))
except Exception as e:
   print("server not available" + str(e.args))
   pass
   

def score(color, tileID, positionUpdate):
   global pmscore
   
   if color == 4:
      if eaten[tileID] != 1:
         pmscore = pmscore+1
      eaten[tileID] = 1
   send_str = (str(pmscore) + ';' + positionUpdate).encode()
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



score(1, 1, 'green:(0,0)')
print("INIT")

for n in range(0, 4):
   cs[n].mode='COL-REFLECT'

while True:
   try:
      for n in range(0, 4):

         # start monitoring if robot is over tile
         if cs[n].mode == 'COL-COLOR':
            if cs[n].value() != 0:
               print( "entering monitoring - color not 0")
               monitoring[n] = 1
         else:
            # reflect mode
            if cs[n].value() > 8:
               monitoring[n] = 1
               print( "entering monitoring - rfl > 8")
               cs[n].mode='COL-COLOR'

         # if we are monitoring then keep stats
         if monitoring[n] == 1:
            valcol = cs[n].value()
            colorcount[n][valcol] = colorcount[n][valcol]+1
            colorcount[n][0] = 0
            colorcount[n][1] = 0
            maxval = max(colorcount[n])
            maxid = colorcount[n].index(maxval)
                           #         print("MAX_COL:"+str(maxid))
                           #         print("TILE NUM:"+str(n+1))
                           #         print("TILE SET:"+str(id))
                           #         print(locations)
            if valcol == 0:
               # robot is no longer on top
               # end monitoring and decide on stats
               locations[colors[maxid]] = (setID-1,n)
               print(colors[maxid]+':'+str(locations[colors[maxid]]))
               score(maxid,n,colors[maxid]+':'+str(locations[colors[maxid]]))
                                   #+":"+str(pmscore))
                                   #            if n+1 == 4:
                                   #               if eaten[counter] != 1:
                                   #                  pmscore = pmscore+1

               # go back to normal mode
               monitoring[n]=0
               if eaten[n] == 1:
                  cs[n].mode='COL-COLOR'
               else:
                  cs[n].mode='COL-REFLECT'
               colorcount[n] = [0]*8
                              #      colorcount = [0,0,0,0,0,0,0,0,0,0,0,0,0,0]

   except Exception as e:
      print(str(e.args))
      pass
        #s.close()
