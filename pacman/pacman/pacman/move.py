#!/usr/bin/python3

# Echo server program
import socket
import ev3dev.ev3 as ev3


B = ev3.LargeMotor('outB')
C = ev3.LargeMotor('outC')
print("INIT")

while True:
#  try:
    HOST = ''                 # Symbolic name meaning all available interfaces
    PORT = 50007              # Arbitrary non-privileged port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    conn, addr = s.accept()
    #print 'Connected by', addr
    ip,port = addr

    with conn:
        print('Connected by', addr)
        while True:
            data = conn.recv(1)
            print(data)
            if not data:
                s.close()
                break
#            conn.sendall(data)
            dir = data.decode()
            if dir == "F":
                  B.run_forever(speed_sp=220)
                  C.run_forever(speed_sp=220)
            elif dir == "B":
                  B.run_forever(speed_sp=-220)
                  C.run_forever(speed_sp=-220)
            elif dir == "L":
                  B.run_forever(speed_sp=200)
                  C.run_forever(speed_sp=-200)
#           B.stop()
#           C.stop()
            elif dir == "R":
                  B.run_forever(speed_sp=-200)
                  C.run_forever(speed_sp=200)
           #B.stop()
#           C.stop()
            elif dir == "S":
                  B.stop()
                  C.stop()
    s.close()
#  except:
#    s.close()
#    pass
