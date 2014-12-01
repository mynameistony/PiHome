#!/bin/bash

while [ 1 ]
do

	/home/pi/printTime.py `date +%l` `date +%M` `date +%P` `date +%a` `date +%h` `date +%d`
	sleep 3

	/home/pi/printIP.py `hostname -I`
	sleep 3
done

exit 0
