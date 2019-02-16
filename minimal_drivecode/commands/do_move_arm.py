# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import PIDCommand
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

		self.kp = 0.5
		self.ki = 0.0
		self.kd = 0.0
		#XXX variable for testing purposes
		self.kf = 0.003

		#self.robot.arm.l_arm_encoder.reset()

		self.final_angle_1 = final_angle
		print(self.final_angle_1)

	def initialize(self):

		# Should move arm when instantiated
		self.pid = wpilib.PIDController(
			self.kp,
			self.ki,
			self.kd,
			self.kf,
			# Gets arm encoder clicks per second
			lambda: self.robot.arm.l_arm_encoder.get_new_rate(),
			# Takes output clicks per sec and shove into given function
			self.robot.arm.set_motors)
		self.pid.reset()

		# Sets tolerable error to return onTarget() to be true, however
		# setAbsoluteTolerance requires setInputRange etc...
		#self.pid.setAbsoluteTolerance(0.5)

		# Clicks per second range
		#self.pid.setInputRange(-318.0, 318.0)
		#self.pid.setOutputRange(-318.0, 318.0)

		# An initial setpoint to boost motor
		#self.pid.setSetpoint(12.0)

		self.pid.setContinuous(False)

		# Turn on pid
		self.pid.enable()
		#XXX debugging neg encoder values
		self.robot.arm.l_arm_encoder.reset()
		print(self.pid.getF())

	def execute(self):
		# Should be continously set based on the current measured angle
		# and returns the velocity the arm should be going to reach
		# the "sweep" angle aka final position of arm. Returned in clicks
		# per second.
		setpoint_rate = self.robot.arm.get_setpoint(self.final_angle_1)
		print("setpoint rate: " + str(setpoint_rate))
		print(self.pid.getSetpoint())
		self.pid.setSetpoint(setpoint_rate)

	def isFinished(self):
		# A "close enough" value; returns true when within the tolerance.
		angle_diff = self.robot.arm.get_current_angle() - self.final_angle_1
		if angle_diff < 0.0:
			angle_diff *= -1

		tolerance = 2.0
		return (angle_diff < tolerance)

	def isInterruptible(self):
		return True

	# This should be redundant because do_arm_interrupt also sets motors to 0
	def end(self):
		self.pid.disable()
		print("Ending Command Do_Move_Arm")
		# Setting motors should not be necessary since disable sets
		# PIDOutput to zero.
		#self.robot.arm.set_motors(0.0)
		#self.cancel()

	def interrupted(self):
		self.end()

