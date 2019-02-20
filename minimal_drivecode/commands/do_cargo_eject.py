# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Eject(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot_cargo = robot.cargo
		self.robot = robot

		# uses motor 6
		
		# Cargo can only be in two states:
		#	1: rotating inwards with Arm at front of robot
		#	2: rotating outwards with Arm at back of robot

		# state 2: possesses Cargo
		self.requires(robot.cargo)

	
	def initialize(self):
		# intake rollers rotate outwards, ejecting ball
		print("cargo eject!")
		self.robot_cargo.cargo_eject()


	def execute(self):
		return None

	def isFinished(self):
		return None

	def end(self):
		self.robot_cargo.cargo_reset()

	def interrupted(self):
		self.end()

