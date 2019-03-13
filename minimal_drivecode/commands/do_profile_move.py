# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig

class Do_Profile_Move(Command):
	'''
	Each time PID is called in commands it can have a different input for
	setpoint which guides how close it is to being at the final position.
	Each different position should have its own final angle.
	'''

	# XXX when directing where to move the arm, the angle which you want to move
	# it to and the direction you want it to move must be supplied
	def __init__(self, robot, end_angle):
		super().__init__()
		print("pid init")
		self.robot = robot
		self.requires(robot.arm)

		self.kp = 1.0
		self.ki = 0.0
		self.kd = 0.001
		#XXX maybe too low; maybe need to tune other parts first
		self.kf = 0.1

		self.end_angle = end_angle

	def initialize(self):

		# Initializes ticks and angle displacement
		self.robot.arm.initialize(self.end_angle)

		# Should move arm when instantiated
		self.pid = wpilib.PIDController(
			self.kp,
			self.ki,
			self.kd,
			self.kf,
			# Gets arm encoder clicks per second
			lambda: self.robot.arm.l_arm_encoder.get_new_rate(),
			# Takes output clicks per sec and shoves into given function
			self.robot.arm.set_motors)

		self.pid.reset()

		self.pid.setContinuous(False)

		# Turn on pid
		self.pid.enable()

	# Continually run by pidloop
	def execute(self):
		if self.robot.arm.back_switch.get():
			self.robot.arm.rearward_limit()
		self.robot.arm.generate(self.end_angle)
		setpoint = self.robot.arm.pick_motor_value()
		self.pid.setSetpoint(setpoint)

	def isFinished(self):
		return False

	def isInterruptible(self):
		return True

	# This should be redundant because do_die_you_gravy_sucking_pig 
	# also sets motors to 0
	def end(self):
		#Don't use min speed. I want the motors to actually stop
		self.robot.arm.set_motors(0, False)
		self.pid.disable()
		self.pid.close()
		print("Do_Move_Arm: Ending Command Do_Move_Arm")

	def interrupted(self):
		self.end()

