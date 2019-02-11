# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Move_Arm(Command):
	'''
	Each time PID is called in commands it can have a different input for
	setpoint which guides how close it is to being at the final position.
	Each different position should have its own final angle.
	'''

	def __init__(self, robot, final_angle):
		super().__init__()
		self.robot = robot
		self.requires(robot.arm)
		self.kp = 1
		self.ki = 0
		self.kd = 0
		self.kf = 0.05
		self.final_angle = final_angle
		self.robot.arm.move_arm(
			self.kp, self.ki, self.kd, self.kf
			) # arg final_angle?
		self.pid = self.robot.arm.pid

	def initialize(self):
		self.pid.reset()
		self.pid.enable()

	def execute(self):
		# Setpoint continuously adjusted
		setpoint_rate = self.robot.arm.get_setpoint(self.final_angle)
		print("setpoint rate: " + str(setpoint_rate))
		self.pid.setSetpoint(setpoint_rate)

	def isFinished(self):
		return None

	def isInterruptible(self):
		return True

	# This should be redundant because do_arm_interrupt also sets motors to 0
	def end(self):
		print("Ending Command Do_Move_Arm")
		self.robot.arm.set_motors(0)
		self.cancel()

	def interrupted(self):
		self.end()

