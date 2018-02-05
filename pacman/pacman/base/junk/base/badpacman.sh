#!/bin/bash
killall nc python2
#python2 -u /home/robot/socketscorer.py &
python2 -u /home/robot/socketscorer.py | nc -k -l -p 1234 &
./exec-py
