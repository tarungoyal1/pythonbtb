from math import sqrt
from time import sleep
def getPrimes():
	def ifPrime(num):
		for i in range(2, int(sqrt(num))+1):
			if num%i==0:
				return False
		return True

	n=3
	while 1:
		if ifPrime(n):
			yield n
		n+=2
	def say(x):
		 return x

if __name__ == "__main__":
	print(2)
	for x in getPrimes():
		print(x)
		sleep(1)
