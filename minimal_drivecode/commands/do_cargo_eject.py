# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Cargo Motor rotates outwards
class Do_Cargo_Eject(Command):
	def __init__(self, robot):
		super().__init__()
		
		# inherited subsystems
		self.robot_cargo = robot.cargo

		# uses motor 6
		'''
		Cargo Intake can only be in two states:
			1: rotating inwards(intake) & Arm at robot front (0 degrees)
			2: rotating outwards(eject) & Arm at robot back (135 degrees)

		State 2: requires Cargo
		'''
		self.requires(robot.cargo)
		
	def initialize(self):
		# intake rollers rotate outwards, ejecting ball
		print("cargo eject!")

		# temp substitute for limit switch. Command lasts 0.2s
		self.setTimeout(0.2)

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

