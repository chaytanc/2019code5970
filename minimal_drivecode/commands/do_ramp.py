# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# actuates Ramp
class Do_Ramp(Command):
	def __init__(self, robot):
		super().__init__()
		
		# inherited subsystems
		self.robot_ramp = robot.ramp

		# uses solenoid 4
		'''
		Ramp can only be in one state:
			1: actuated with Arm at [UNKNOWN POSITION]

		State 1: requires Ramp
		'''
		self.requires(self.robot_ramp)

	
	def initialize(self):
		# actuate Ramp
		self.robot_ramp.ramp_actuate()
		print("Ramp Deployed!!")

	def execute(self):
		return None

	def isFinished(self):
		return True

	def end(self):
		return None

	def interrupted(self):
		self.robot_ramp.ramp_unactuate()
		print("Command 'ramp' interrupted!")
		self.end()

