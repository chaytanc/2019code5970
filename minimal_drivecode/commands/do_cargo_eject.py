# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Eject(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot_cargo = robot.cargo

		# uses motor 6
		
		# Cargo can only be in two states:
		#	1: rotating inwards with Arm at front of robot
		#	2: rotating outwards with Arm at back of robot

		# state 2: possesses Cargo
		self.requires(robot.cargo)
		

	def initialize(self):
		# intake rollers rotate outwards, ejecting ball
		print("cargo eject!")

		# temp substitute for limit switch. Command lasts 0.5s
		self.setTimeout(0.5)

	def execute(self):
		# move to initialize when limit switches are implemented 
		# and replace timeout
		self.robot_cargo.cargo_eject()

	def isFinished(self):
		return self.isTimedOut()

	def end(self):
		# reset cargo motor speed to 0 at end of command
		self.robot_cargo.cargo_reset()

	def interrupted(self):
		print("Command 'cargo_eject' interrupted!")		
		self.end()

