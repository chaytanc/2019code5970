# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import PIDCommand
from wpilib.command import Command
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig

class Do_Move_Arm(Command):
	'''
	Each time PID is called in commands it can have a different input for
	setpoint which guides how close it is to being at the final position.
	Each different position should have its own final angle.
	'''

	# XXX when directing where to move the arm, the angle which you want to move
	# it to and the direction you want it to move must be supplied
	def __init__(self, robot, final_angle):
		super().__init__()
		print("pid init")
		self.robot = robot
		self.requires(robot.arm)

		self.kp = 1.0
		self.ki = 0.0
		self.kd = 0.0

		#XXX maybe too low; maybe need to tune other parts first
		self.kf = 1.0

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
		'''
		# Tentative PID using angles as input/output
		self.pid = wpilib.PIDController(
			self.kp,
			self.ki,
			self.kd,
			self.kf,
			# Gets arm encoder clicks per second
			lambda: self.robot.arm.l_arm_encoder.get_angle(),
			# Takes output clicks per sec and shove into given function
			self.robot.arm.set_motors)
		'''

		self.pid.reset()

		# Sets tolerable error to return onTarget() to be true, however
		# setAbsoluteTolerance requires setInputRange etc...
		#self.pid.setAbsoluteTolerance(0.5)

		# Clicks per second range
		#self.pid.setInputRange(-10.0, 10.0)
		#self.pid.setOutputRange(-10.0, 10.0)

		self.pid.setContinuous(False)
		

		# Turn on pid
		self.pid.enable()
		#XXX debugging neg encoder values
		print(self.pid.getF())

	def execute(self):
		# Should be continously set based on the current measured angle
		# and returns the velocity the arm should be going to reach
		# the "sweep" angle aka final position of arm. Returned in clicks
		# per second.
		#setpoint_rate = self.robot.arm.get_setpoint(self.final_angle_1)
		#print("setpoint rate: " + str(setpoint_rate))
		#print(self.pid.getSetpoint())
		#self.pid.setSetpoint(setpoint_rate)
		self.pid.setSetpoint(self.final_angle_1)
		print("pid input " + str(self.robot.arm.l_arm_encoder.get_new_rate()))
		#print ("pid error " + str(self.pid.getError()))
		#print ("output " + str(self.pid.get()))

	def isFinished(self):
		# A "close enough" value; returns true when within the tolerance.

		#angle_diff = abs(self.final_angle_1 - self.robot.arm.get_current_angle())

		#tolerance = 2.0
		#return (angle_diff < tolerance)
		return False

	def isInterruptible(self):
		return True

	# This should be redundant because do_die_you_gravy_sucking_pig 
	# also sets motors to 0
	def end(self):
		#Don't use min speed. I want the motors to actually stop
		#self.robot.arm.set_motors(0, False)
		self.pid.disable()
		self.pid.close()
		print("Do_Move_Arm: Ending Command Do_Move_Arm")

	def interrupted(self):
		#self.robot.arm.reset_motors()
		self.end()


