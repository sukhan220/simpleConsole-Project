
from time import *
while True:
	#input how many times
	# want to count down
	Value = int(input("Count Down >> "))

	#loop for Value to 0
	for i in range(Value,-1,-1):
        #get quotient
		#without point(//)
		m=Value//60
		second=str(Value%60)
		hour=str(m//60)
		minute=str(m%60)
		CountDown = hour.zfill(2) + ":" + minute.zfill(2) + ":" + second.zfill(2)
		print(CountDown + "\r", end="")
        #delay one second
		sleep(1)

		#CountDown value decrease
		Value -= 1
	print()
