# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class EncoderCheck(Command):
	"""
	Check and return values from encoder 
	"""

	def __init__(self, robot):
		super().__init__()

		self.robot = robot
		self.requires(self.robot.encoders)
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
	
	def execute(self):
		"""Called repeatedly when this Command is scheduled to run"""
		self.robot.encoders.get_direction()
		# Get encoder values 
	
	def isFinished(self):
		"""Make this return true when this Command no longer needs to run execute()"""
		return False #loop until robot is powered off

	def end(self):
		"""Called once after isFinished returns true"""

	def interrupted(self):
		"""Called when another command which requires one or more of the same subsystems is scheduled to run"""

	
