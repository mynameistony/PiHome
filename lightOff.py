import serial

ser = serial.Serial('/dev/ttyAMA0', 9600, timeout=1)
ser.open()

ser.write(chr(18))

ser.close()
