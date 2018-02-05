import time
locations = {"none": (0,0), "black": (0,0), "blue" : (0,0),"green": (0,0),"yellow": (0,0),"red": (0,0),"white": (0,0), "brown": (0,0)}
file = open("locations.txt","w")


def follow(thefile):
    thefile.seek(0,2)
    while True:
        line = thefile.readline()
        if not line:
            time.sleep(0.01)
            continue
        yield line

if __name__ == '__main__':
    logfile = open("colors","r")
    loglines = follow(logfile)
    for line in loglines:
#        print line,
	color = line.split(':')[0]
#	print color
	coord = line.split(':')[1].split('\n')[0]
#	print coord
	locations[color] = coord
	print locations
	file.write(str(locations)+"\n")
file.close()
