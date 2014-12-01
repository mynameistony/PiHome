#!/usr/bin/python

import serial
import sys
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)


hour=sys.argv[1]
min=sys.argv[2]
am=sys.argv[3]
dow=sys.argv[4]
month=sys.argv[5]
dom=sys.argv[6]

ser.open()
ser.write(chr(12))
ser.write(dow)
ser.write(", ")
ser.write(month)
ser.write(" ")
ser.write(dom)

ser.write(chr(13))

ser.write(hour)
ser.write(":")
ser.write(min)
ser.write(am)

ser.close()

