# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Ramp(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		self.robot_arm = robot.arm

		self.requires(self.robot_arm)
        
		self.ramp_solenoid = self.robot_arm.ramp_solenoid
		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
	
	def initialize(self):
		return None
	def execute(self):
		self.robot_arm.ramp_actuate(self.ramp_solenoid)
		print("Ramp Deployed!!")

		# Required periodical call to Differential Drive
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
		self.robot_arm.ramp_unactuate(self.ramp_solenoid)
		self.end()

