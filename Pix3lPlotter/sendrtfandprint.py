import os,time
while True:
	os.system('	./pixel2ev3.py image.png > image.rtf')
	os.system('scp image.rtf root@192.168.1.11:/mnt/ramdisk/prjs/plotter_wheel_ppwi/image.rtf')
	os.system("ssh root@192.168.1.11 'echo 1 > /mnt/ramdisk/prjs/plotter_wheel_ppwi/lock.rtf'") 
	done = "0"
	while done != "1":
		os.system('scp root@192.168.1.11:/mnt/ramdisk/prjs/plotter_wheel_ppwi/done.rtf .')
		done = os.popen('cat done.rtf').read().split('\n')[0]
		time.sleep(0.1)
		print "Done: " +str(done)
