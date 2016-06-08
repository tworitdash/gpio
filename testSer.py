import serial
ser=serial.Serial("/dev/ttyAMA0", 9600, timeout=1)

while True:
	#w=(input("Enter input:"))
	ser.write(str.encode('q'))
	data=ser.readline()
	print(data)
	ser.write(str.encode('%' + 'w' +'%'))
