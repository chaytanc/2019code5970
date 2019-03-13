# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import Subsystem
#from wpilib import InterruptableSensorBase

class Back_Switch():
	"""
	Collect events from the back limit switch of the arm.
	"""
	def __init__(self):
		super().__init__()
	'''
		# Back limit switch of arm

		self.back_switch = wpilib.DigitalInput(8)
		#self.counter = wpilib.Counter(self.switch)
		#self.counter.reset()

			
