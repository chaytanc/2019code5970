# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
from wpilib import DigitalInput

# positions Arm to robot back for calibrating autonomous
class Do_Basic_Move_Arm(Command):
	def __init__(self, robot, motor_speed):
		super().__init__()
		# instantiate motor_speed and timeout variables
		self.motor_speed = motor_speed

		self.limit_switch = robot.arm.limit_switch

		# inherited subsystems
		self.robot_arm = robot.arm

		# uses motors ctre 1 and 3
		'''
		Basic Arm Movement can only be in one state:
			1: Position Arm to robot front(180 degrees) at autonomousInit

		State 1: possesses Arm
		'''
		self.requires(robot.arm)
		
	def initialize(self):
		# move arm backwards by setting motor speed to negative value
		self.robot_arm.arm_motors.left_arm_motor.set(self.motor_speed)
		self.robot_arm.arm_motors.right_arm_motor.set(-self.motor_speed)
		print("setting arm motor speed to: " + str(self.motor_speed))

	def execute(self):

		#print("encoder count: " + str(self.robot_arm.l_arm_encoder.getDistance()))		
		print(self.limit_switch.get())

		return None

	def isFinished(self):
		if not self.limit_switch.get():
			return True
		#return None

	def end(self):
		# stop arm ctre motors at end of command
		self.robot_arm.arm_motors.left_arm_motor.stopMotor()
		self.robot_arm.arm_motors.right_arm_motor.stopMotor()

	def interrupted(self):
		print("Command 'basic_move_arm' interrupted!")
		self.end()

