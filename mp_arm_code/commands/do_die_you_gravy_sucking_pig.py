# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Die_You_Gravy_Sucking_Pig(Command):

	def __init__(self, robot):
		super().__init__()
		self.requires(robot.arm)
		self.robot_arm = robot.arm

	def initialize(self):
		print("Ran Command Do_Die_You_Gravy_Sucking_Pig")
		return None

	def execute(self):
		self.robot_arm.arm_motors.set_speed(0)

	def isFinished(self):
		return None

	def end(self):
		return None

	def interrupted(self):
		self.end()
