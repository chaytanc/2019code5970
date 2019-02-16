# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
import sys
sys.path.append('..')

class Do_Encoder_Check(Command):
	"""
	Check and return values from encoder 
	"""

	def __init__(self, robot):
		
		super().__init__()
		self.robot_arm = robot.arm

		self.requires(self.robot_arm)
		self.setTimeout(1)

		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy

		self.left_e = self.robot_arm.l_arm_encoder

	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.left_e.reset()

	def execute(self):
		"""Called repeatedly when this Command is scheduled to run"""
		# Print return value here, as get_direction() 
		# may be used for both encoders, which would require two returns
		print("Arm Encoder: " + str(self.robot_arm.get_click_rate()))
		#print(self.robot_arm.sin_relative_angle(45, 35))
		# Get encoder values 

	def isFinished(self):
		"""Make this return true when this Command no longer needs to run execute()"""
		return self.isTimedOut()

	def end(self):
		"""Called once after isFinished returns true"""
		return None


	def interrupted(self):
		"""Called when another command which requires one or more of the same subsystems is scheduled to run"""
		self.end()

	

