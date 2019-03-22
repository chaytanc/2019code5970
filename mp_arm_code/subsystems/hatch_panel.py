# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Hatch_Panel(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		super().__init__()
		'''
		Command Dependencies:
			Hatch Panel Intake/Eject

		Initialize Pneumatics[hatch panel intake]
			Each solenoid is instantiated by 
			an "actuated" and "unactuated" command 
			(intake and eject, respectively)
		'''
		self.hp_solenoid = wpilib.Solenoid(2)

	# Arm must be in position before actuate/unactuate
	def hp_actuate(self):
		# actuate hatch panel intake solenoid & corresponding pistons
		self.hp_solenoid.set(True)

	def hp_unactuate(self):
		# actuate hatch panel intake solenoid & corresponding pistons
		self.hp_solenoid.set(False)


