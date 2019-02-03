# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../oi')
#from oi import OI

class Do_Tank_Drive(Command):

	def __init__(self, robot):
		# Recognize as a wpilib command
		print("***********************")
		print(str(robot))
		print("***********************")
		super().__init__()

		# an instance of BeaverTronicsRobot from robot.py containing its
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		#self.oi = OI(self)
		self.requires(self.robot_dt)
		self.left_joy = robot.oi.left_joy
		self.right_joy = robot.oi.right_joy

	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		
	
	def execute(self):
		# Continuously sets motor speed to joystick inputs w/ Scheduler
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)

		# Currently cannot find way to reference left_speed in drivetrain.py
		# Using left_joy as functional substitute
		print("left_speed: " + str(self.left_joy.getY()))


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


	
