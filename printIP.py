#!/usr/bin/python
import serial
import sys
import time


ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)

ser.open()

ser.write(chr(12))

ip=sys.argv[1]

ser.write("IP Address: ")
ser.write(chr(13))
ser.write(ip)

ser.close()

