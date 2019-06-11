#!/bin/bash
sshpass -vp maker scp -vr pacman/ robot@192.168.0.3:~/
sshpass -vp maker scp -vr pacman/ robot@192.168.0.5:~/
sshpass -vp maker scp -vr pacman/ robot@192.168.0.7:~/
