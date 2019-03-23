# vim: set sw=4 noet ts=4 fileencoding=utf-8:

#XXX ERRORS OUT IN SIM
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
		self.kd = 0.0
		#XXX maybe too low; maybe need to tune other parts first
		self.kf = 0.16

		self.end_angle = end_angle

	def initialize(self):


		# Should move arm when instantiated
		self.pid = wpilib.PIDController(
			self.kp,
			self.ki,
			self.kd,
			self.kf,
			# Gets arm encoder clicks per second
			self.robot.arm.arm_motors.left_arm_motor.get,
			# Takes output clicks per sec and shoves into given function
			self.robot.arm.set_motors)

		self.pid.reset()

		self.pid.setContinuous(False)

		# Turn on pid
		self.pid.enable()

		#XXX
		# Initializes ticks and angle displacement
		self.robot.arm.initialize()
		self.robot.arm.generate(self.end_angle)

	# Continually run by pidloop
	def execute(self):
		if not self.robot.arm.back_switch.get():
			print("Do_Profile_Move: limit: " 
					+ str(self.robot.arm.back_switch.get())
					)
			self.robot.arm.rearward_limit()
		try:
			setpoint = self.robot.arm.pick_motor_value()
			print("Do_Profile_Move: setpoint: " + str(setpoint))
			self.pid.setSetpoint(setpoint)
			print("Do_Profile_Move: pid output: " + str(self.pid.get()))

		# Handles arm going past the end angle
		except IndexError:
			self.pid.setSetpoint(self.robot.arm.vp[-1])

	def isFinished(self):
		return False

	def isInterruptible(self):
		return True

	# This should be redundant because do_die_you_gravy_sucking_pig 
	# also sets motors to 0
	def end(self):
		#Don't use min speed. I want the motors to actually stop
		self.robot.arm.set_motors(0)
		self.pid.disable()
		self.pid.close()
		print("Do_Move_Arm: Ending Command Do_Move_Arm")
		#XXX NEED TO RAISE RUNTIME EXCEPTION IF ARM GOES PAST END ANGLE IT
		# GOES OUT OF INDEX OF SETPOINTS SO NEED TO SET TO LAST ELEMENT OF 
		# SETPOINT INDEX

	def interrupted(self):
		self.end()

