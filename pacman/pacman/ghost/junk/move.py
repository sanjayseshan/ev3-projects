import time,os
import ev3dev.ev3 as ev3


B = ev3.LargeMotor('outB')
C = ev3.LargeMotor('outC')



def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.01)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("directions","r")
    loglines = follow(logfile)
    for line in loglines:
     dir = line.split('\n')[0]
     print(line)
     if dir == "FORWARD":
           B.run_forever(speed_sp=300)
           C.run_forever(speed_sp=300)
     elif dir == "BACKWARD":
           B.run_forever(speed_sp=-300)
           C.run_forever(speed_sp=-300)
     elif dir == "LEFT":
           B.run_forever(speed_sp=300)
           C.run_forever(speed_sp=-300)
#           B.stop()
#           C.stop()
     elif dir == "RIGHT":
           B.run_forever(speed_sp=-300)
           C.run_forever(speed_sp=300)
           #B.stop()
#           C.stop()
     elif dir == "STOP":
           B.stop()
           C.stop()

#	locations[color] = coord
#	print locations
