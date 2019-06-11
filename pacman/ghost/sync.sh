#!/bin/bash
sshpass -vp maker scp -vr pacman/ robot@192.168.0.2:~/
sshpass -vp maker scp -vr pacman/ robot@192.168.0.4:~/
sshpass -vp maker scp -vr pacman/ robot@192.168.0.6:~/
