#!/bin/bash
cd ~/
echo "Running Pacman for EV3 v2.5.1"
echo 'raspberry' | sudo -S killall python tcpdump ssh sshpass
sshpass -p raspberry ssh pi@localhost '~/exec-pacman'

