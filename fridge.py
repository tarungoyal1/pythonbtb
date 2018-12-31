"""Healthy Refrigerator Raider"""

from contextlib import closing

class Refrigerator:

	def open(self):
		print("Opening Refrigerator")

	def take(self, food):
		print("Searching for {}".format(food))
		badfood = ['pizza', 'pepsi', 'burger', 'french fries', 'sugar', 'coke', 'cheese sandwich']
		if food in badfood:
			raise RuntimeError("Health warning! Detrimental to your health")
		print("Taking {}".format(food))

	def close(self):
		print("Closing Refrigerator")

def raid(food):
	with closing(Refrigerator()) as r:
	    r.open()
	    try:
	    	r.take(food)
	    except RuntimeError as e:
	    	print(e)