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
		self.ki = 0
		self.kd = 0
		self.kf = 0.06

		# Should move arm when instantiated
		# XXX from self.move_arm to here trying to debug
		self.pid = wpilib.PIDController(
			self.kp,
			self.ki,
			self.kd,
			self.kf,
			# Gets arm encoder clicks per second
			self.robot.arm.l_arm_encoder.getRate,
			# Takes output clicks per sec and shove into given function
			self.robot.arm.set_motors)
		self.pid.setAbsoluteTolerance(0.5)
		self.pid.setInputRange(-100.0, 100.0)
		self.pid.setSetpoint(12.0)
		self.pid.setOutputRange(-100.0, 100.0)
		self.pid.setContinuous(False)
#		self.robot.arm.move_arm(
#			self.kp, self.ki, self.kd, self.kf
#			)

		self.final_angle_1 = final_angle
		print(self.final_angle_1)

	def initialize(self):
		self.pid.reset()
		self.pid.enable()
		print(str(self.pid.isEnabled()))
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
		return None

	def isInterruptible(self):
		return True

	# This should be redundant because do_arm_interrupt also sets motors to 0
	def end(self):
		self.pid.disable()
		print("Ending Command Do_Move_Arm")
		self.robot.arm.set_motors(0)
		self.cancel()

	def interrupted(self):
		self.end()

