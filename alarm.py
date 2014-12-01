import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write(chr(213))

for i in range(0,10):
	ser.write(chr(220))

ser.close()
