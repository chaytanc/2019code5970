# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../oi')
#from oi import OI

class Cargo_Test(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command

		super().__init__()

		# an instance of BeaverTronicsRobot from robot.py containing its
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		#self.oi = OI(self)
		self.requires(self.robot_dt)
		self.third_joy = robot.third_joy

	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		
	
	def execute(self):
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.robot_dt.cargo_intake_test(
			self.third_joy, self.robot_dt.drive)


	def isFinished(self):
		# This is how running tank driving is prioritized
		# In other words, runs til interrupted
		return False

	def end(self):
		# Stop motors when ending command
		self.robot_dt.stop_robot(self.robot_dt.drive)
	
	### Maybe don't want to stop motors when interrupted
	def interrupted(self):
		self.end()


	