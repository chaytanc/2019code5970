# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

class Hp_Intake(Subsystem):
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
		# BEAK
		self.beak = wpilib.Solenoid(2)

		# 4 BAR
		self.bars = wpilib.Solenoid(3)

	# OPENS beak
	def beak_actuate(self):
		self.beak.set(True)

	# CLOSES BEAK
	def beak_unactuate(self):
		self.beak.set(False)

	def bars_actuate(self):
		# actuate 4 bar pistons such that beak is out of frame 
		self.bars.set(True)

	def bars_unactuate(self):
		# actuate hatch panel intake solenoid & corresponding pistons
		self.bars.set(False)


