# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
import sys
sys.path.append('..')

class Do_Motor_Rate_Test(Command):
	"""
	Check and return values from encoder 
	"""

	def __init__(self, robot):
		
		super().__init__()
		self.robot_dt = robot.drivetrain
		self.arm = robot.arm

		self.requires(self.robot_dt)
		self.requires(self.arm)

		self.setTimeout(0.1)

		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
		
		# Motor Encoder Here
		self.arm_e = self.arm.l_arm_encoder

	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.arm_e.reset()

	def execute(self):
		"""Called repeatedly when this Command is scheduled to run"""


		self.arm.motor_test_max_speed()
		print(self.arm.direction)

		# Required periodical call to Differential Drive
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
		"""Make this return true when this Command no longer needs to run execute()"""
		return self.isTimedOut()

	def end(self):
		"""Called once after isFinished returns true"""
		return None


	def interrupted(self):
		"""Called when another command which requires one or more of the same subsystems is scheduled to run"""
		self.end()

	

