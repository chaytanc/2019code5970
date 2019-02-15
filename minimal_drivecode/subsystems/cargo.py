# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import math
import wpilib
from wpilib.command import Subsystem

# Control cargo intake

class Cargo(Subsystem):

	def __init__(self, robot):
		print("init")
		super().__init__()
		self.cargo_motor = wpilib.VictorSP(7)

	def cargo_intake(self, motor):
		#self.set_arm_position(intake)
		motor.set(1)

	def cargo_reset(self, motor):
		motor.set(0)
			
	# Actually ejects ball. Arm must be set correctly beforehand
	def cargo_eject(self, motor):
		# Cargo ball motor
		motor.set(-1)

