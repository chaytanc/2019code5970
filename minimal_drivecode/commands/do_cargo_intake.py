# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
		
# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Intake(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		self.robot_cargo = robot.cargo
		
		self.cargo_motor = robot.cargo.cargo_motor
		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
	
	def initialize(self):
		return None
	def execute(self):
		self.robot_cargo.cargo_intake(self.cargo_motor)
		print("cargo intake!")

		# Required periodical call to Differential Drive
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
		return None
	def end(self):
		self.robot_cargo.cargo_reset(self.cargo_motor)
	def interrupted(self):
		self.end()
