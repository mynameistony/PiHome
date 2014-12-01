import random
import serial
import time

f = open('/home/pi/facts.txt')
randNum = random.randrange(0,20)

for i in range(0,20):
       	thisLine = f.readline()
        if(i == randNum):
		ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
		ser.open()
		ser.write(chr(128))
		counter = int(0)
		for i in thisLine:
			counter += 1
			if(counter % 16 == 0):
				time.sleep(2)
				ser.write(chr(128))				
		                for j in range(0,16):					
                		        ser.write(' ')
				ser.write(chr(128))
			ser.write(i)
			print counter
			print i
		time.sleep(1)
		ser.close()

f.close()
