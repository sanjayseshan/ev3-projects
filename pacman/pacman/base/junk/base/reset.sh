#!/bin/bash

./exec-py &
sleep 1
sshpass -p maker ssh 192.168.0.1 '~/exec-master' &
sleep 1
sshpass -p maker ssh 192.168.0.3 '~/exec-master' &
sleep 1
sshpass -p maker ssh 192.168.0.5 '~/exec-master' &
