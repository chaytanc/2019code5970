# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

# Control cargo intake

class Cargo(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self, robot):
		print("init")
		super().__init__()
		# Command Dependencies:
		#	Cargo Intake/Eject

		# Initialize Motor[cargo intake]
		#	Cargo is instantiated by 
		#	an "intake" and "eject" command
		self.cargo_motor = wpilib.VictorSP(6)

	# Arm must be in position before intake/eject
	def cargo_intake(self):
		# motor rotates inward to intake ball
		# 0.25 test intake value
		self.cargo_motor.set(0.75)

	def cargo_eject(self):
		# motor rotates outward to eject ball
		self.cargo_motor.set(-0.75)

	def cargo_reset(self):
		# resets motor to 0 speed
		self.cargo_motor.set(0)
			


