# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

from sys import path
path.append('../')

# command groups
from command_cargo_eject import Command_Cargo_Eject
from command_cargo_intake import Command_Cargo_Intake

# Control cargo intake

class Cargo(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self, robot):
		print("init")
		super().__init__()
		self.robot = robot
		'''
		Command Dependencies:
			Cargo Intake/Eject

		Initialize Motor[cargo intake]
			Cargo is instantiated by 
			an "intake" and "eject" command
		'''
		self.cargo_motor = wpilib.VictorSP(6)

	# Arm must be in position before intake/eject
	def cargo_intake(self):
		# motor rotates inward to intake ball
		# 0.25 test intake value
		self.cargo_motor.set(0.35)

	def cargo_eject(self):
		# motor rotates outward to eject ball
		self.cargo_motor.set(-0.35)

	def cargo_reset(self):
		# resets motor to 0 speed
		self.cargo_motor.set(0)

	def cargo_axis_commands(self, current_axis_input, previous_axis_input):
		# responds to xbox button 5 axis
		
		# when axis is negative, run Command_Cargo_Eject once
		if current_axis_input <= -0.4 and previous_axis_input >= -0.3:
			Command_Cargo_Eject(self.robot).start()

		# when axis is positive, run Command_Cargo_Intake once
		if current_axis_input >= 0.4 and previous_axis_input <= 0.3:
			 Command_Cargo_Intake(self.robot).start()

			

