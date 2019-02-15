# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#import wpilib
from wpilib.command import Command

class Do_Move_Arm_NoPID(Command):
	'''
	'''

	def __init__(self, robot, final_angle):
		super().__init__()
		self.requires(robot.arm)

		self.robot = robot
		self.final_angle = final_angle
		print("__init__ of do_move_arm_nopid")

	def initialize(self):
		self.last_rate = 0.0
		print("initialize of do_move_arm_nopid")

	def execute(self):
		rate = self.robot.arm.get_click_rate()
		if rate != self.last_rate:
			self.last_rate = rate
			print("New encoder click rate: " + str(rate))

		voltage = self.robot.arm.sin_angle(self.final_angle)
		rate = self.robot.arm.voltage_to_click_rate(voltage)
		self.robot.arm.set_motors(rate, True)

	def isFinished(self):
		angle = self.robot.arm.get_current_angle()
		diff = self.abs(angle - self.final_angle)
		print("**** angle: " + str(angle) + " target: " + str(self.final_angle))
		done = (diff < 2.0)

		return done

	def end(self):
		print("Ending Command Do_Move_Arm_NoPID")
		self.robot.arm.set_motors(0.0)

	def isInterruptible(self):
		return True

	def interrupted(self):
		self.end()

	def abs(self, value):
		if value < 0.0:
			return -value
		else:
			return value
