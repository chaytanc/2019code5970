# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Ramp(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		super().__init__()
		'''
		Command Dependencies:
			Ramp Actuation (do_ramp.py)
		
		Initialize Pneumatics[ramp]
			This solenoid is instantiated by 
			only an "actuated" command

			Ramp is manually unactuated. Unactuated function exists for safety
		'''
		self.ramp_solenoid = wpilib.Solenoid(4)

	def ramp_actuate(self):
		# actuate ramp
		self.ramp_solenoid.set(True)

	def ramp_unactuate(self):
		# unactuate ramp, for emergencies
		self.ramp_solenoid.set(False)

