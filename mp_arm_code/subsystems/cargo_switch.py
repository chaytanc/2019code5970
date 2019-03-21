# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import Subsystem
#from wpilib import InterruptableSensorBase

class Cargo_Switch(Subsystem):
	"""
	Collect events from the back limit switch of the arm.
	"""
	def __init__(self):
		super().__init__()
		#Back limit switch of arm
		self.switch = wpilib.DigitalInput(9)
		self.counter = wpilib.Counter(self.switch)
		self.counter.reset()

	def check_counter(self):
		self.hit_limit = (self.counter.get() > 0)
		return self.hit_limit 
 
