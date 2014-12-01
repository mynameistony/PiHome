#!/usr/bin/python

import os
import serial
import time
from time import gmtime, strftime, localtime

currTime = strftime("%I%M",localtime())
currHour = strftime("%I",localtime())
currMin = strftime("%M",localtime())
AM = strftime("%p",localtime())

f = open('/home/pi/alarm.txt', 'r')


alarmHour = f.readline().strip('\n')
alarmMin = f.readline().strip('\n')
alarmAM = f.readline().strip('\n')

f.close()
if(alarmAM == 'p'):
	alarmAM = "PM"
else:
	 alarmAM = "AM"

print alarmHour
print alarmMin
print alarmAM

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

if(alarmHour == currHour):
	if(alarmMin == currMin):
		if(alarmAM == AM):
			os.system('python /home/pi/alarm.py')

print "Printing time"

ser.write(chr(17))
ser.write(chr(12))
ser.write(chr(148))
ser.write(currHour)
ser.write(":")
ser.write(currMin)
ser.write(AM)
ser.write(" ")
ser.write(alarmHour)
ser.write(":")
ser.write(alarmMin)
ser.write(alarmAM)
ser.close()

