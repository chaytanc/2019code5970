# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Hatch_Panel_Rotate(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		super().__init__()
		'''
		Command Dependencies:
			Hatch Panel Rotate Actuated/Unactuated

		Initialize Pneumatics[hatch panel intake]
			Each solenoid is instantiated by 
			an "actuated" and "unactuated" command
		'''
		self.hp_rotate_solenoid = wpilib.Solenoid(3)

	# Arm must be in position before actuate/unactuate
	def hp_actuate(self):
		# actuate hatch panel rotation solenoid & corresponding pistons
		self.hp_rotate_solenoid.set(True)

	def hp_unactuate(self):
		# actuate hatch panel rotation solenoid & corresponding pistons
		self.hp_rotate_solenoid.set(False)


