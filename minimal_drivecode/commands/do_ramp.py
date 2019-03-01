# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Ramp(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		self.robot_ramp = robot.ramp
		self.robot = robot
		# uses solenoid 4
		
		# Ramp can only be in one state:
		#	1: actuated with Arm at ????

		# state 1: possesses Ramp
		self.requires(self.robot_ramp)

	
	def initialize(self):
		return None
	def execute(self):
		self.robot_ramp.ramp_actuate()
		print("Ramp Deployed!!")
	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
		self.robot_ramp.ramp_unactuate()
		print("Command 'ramp' interrupted!")
		self.end()

