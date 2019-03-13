# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
		
# Cargo Motor rotates inwards
class Do_Cargo_Intake(Command):
	def __init__(self, robot):
		super().__init__()
		
		# inherited subsystems
		self.robot_cargo = robot.cargo

		# uses motor 6
		'''
		Cargo Intake can only be in two states:
			1: rotating inwards(intake) & Arm at robot back (0 degrees)
			2: rotating outwards(eject) & Arm at robot front (135 degrees)

		State 1: requires Cargo
		'''
		self.requires(robot.cargo)

	def initialize(self):
		# intake rollers rotate inwards, intaking ball
		print("cargo intake!")
		
		# temp substitute for limit switch. Command lasts 0.2s
		self.setTimeout(0.5)

	def execute(self):
		# move to initialize when limit switches are implemented 
		# and replace timeout
		self.robot_cargo.cargo_intake()

	def isFinished(self):
		#return self.isTimedOut()
		return None

	def end(self):
		# reset cargo motor speed to 0 at end of command
		self.robot_cargo.cargo_reset()

	def interrupted(self):
		print("Command 'cargo_intake' interrupted!")
		self.end()
