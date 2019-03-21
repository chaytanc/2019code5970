# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
#import sys
#sys.path.append('..')

class Do_Max_Arm_Speed(Command):
#class Do_Motor_Rate_Test(Command):
	"""
	Check and return values from encoder 
	"""

	def __init__(self, robot):
		super().__init__()

		self.max_speed = 0.0
		self.setTimeout(0.15)
		
		self.arm = robot.arm
		self.requires(self.arm)

		# Arm Encoder Here
		self.encoder = self.arm.l_arm_encoder

	def initialize(self):
		"""Called just before this Command runs the first time"""
		self.encoder.reset()
		self.arm.motor_test_max_speed()

	def execute(self):
		"""Called repeatedly when this Command is scheduled to run"""
		rate = self.arm.get_click_rate()

		if rate < 0.0:
			raise RuntimeError("speed is negative in arm speed test")

		if rate > self.max_speed:
			self.max_speed = rate

	def isFinished(self):
		"""
		Make this return true when this Command no longer needs
		to run execute()
		"""
		return self.isTimedOut()

	def end(self):
		"""Called once after isFinished returns True"""
		self.arm.arm_motors.set_speed(0.0)
		print("==== MAXIMUM ARM SPEED: " + str(self.max_speed) + " ====")
		return None

	def interrupted(self):
		"""
		Called when another command which requires one or more of the
		same subsystems is scheduled to run.
		"""
		self.arm.arm_motors.set_speed(0.0)
		self.end()
