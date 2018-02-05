import ev3dev.ev3 as ev3
import time

ult1 = ev3.UltrasonicSensor(address='ev3-ports:in1')
ult2 = ev3.UltrasonicSensor(address='ev3-ports:in2')
ult3 = ev3.UltrasonicSensor(address='ev3-ports:in3')
ult4 = ev3.UltrasonicSensor(address='ev3-ports:in4')

#print("INIT")

while True:
#	print("SET")
#	print(ult1.value())
#	print(ult2.value())
#	print(ult3.value())
#	print(ult4.value())
	if ult1.value() < 70:
		print("FORWARD")
		while ult1.value() < 70:
			nnn=0
	elif ult2.value() < 70:
		print("RIGHT")
		while ult2.value() < 70:
			nnn=0
	elif ult3.value() < 70:
		print("BACKWARD")
		while ult3.value() < 70:
			nnn=0
	elif ult4.value() < 70:
		print("LEFT")
		while ult4.value() < 70:
			nnn=0
	else:
		print("STOP")
		while ult1.value() > 70 and ult2.value() > 70 and ult3.value() > 70 and ult4.value() > 70:
			nnn=0


#	print("END SET")
#	time.sleep(0.1)
