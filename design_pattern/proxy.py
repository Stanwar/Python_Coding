#### Proxy 

import time

class Producer():
	""" Resource Intensive Class """
	def produce(self):
		print "Producer is working"

	def meet(self):
		print "Producer has time to meet now!"

class Proxy:
	""" Handles work till producer class gets free """
	def __init__(self):
		self.occupied = 'No'
		self.producer = None

	def produce(self):
		print "Artist checking if procuder is available"

		if self.occupied == 'No':
			self.producer = Producer()
			time.sleep(2)

			self.producer.meet()
		else:
			time.sleep(2)
			print "Producer is busy"

p = Proxy()

p.produce()

p.occupied = 'Yes'

p.produce()