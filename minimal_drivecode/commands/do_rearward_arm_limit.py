# vim: set sw=4 noet ts=4 fileencoding=utf-8:
"""
Created on Sun Feb 10 13:43:06 2019

@author: noahm
"""
from wpilib.command import Command

class Do_Rearward_Arm_Limit(Command):
	def __init__(self, robot):
		self.requires(robot.arm)
		robot.arm.l_arm_encoder = 403.2 * (140.48 / 180.0)
		robot.arm.arm_motors.set_speed(0)

	def execute():
		pass

	def isFinished():
		return True

	def end():
		pass

	def interrupted():
		pass
