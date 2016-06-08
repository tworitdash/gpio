numTimes = int(input("enter no of iterations:"))
speed = float(input("enter length of blink:"))


import RPi.GPIO as g
import time
g.setmode(g.BOARD)
g.setup(7,g.OUT)



for i in range(0,numTimes):
	print ("Iteration" + str(i+1))
	g.output(7,True)
	time.sleep(speed)
	g.output(7,False)
	time.sleep(speed)
print ("Done")
g.cleanup()
