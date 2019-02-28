# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Moves arm to back of robot
class Do_Basic_Move_Arm(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot_arm = robot.arm

		# uses motors ctre 1 and 3
		
		# Basic Arm Movement can only be in one state:
		#	1: Move arm to back of robot at beginning of match 

		# state 1: possesses Arm
		self.requires(robot.arm)
		

	def initialize(self):
		# move arm backwards by setting motor speed to negative value
		self.robot_arm.arm_motors.left_arm_motor.set(-0.2)
		self.robot_arm.arm_motors.right_arm_motor.set(-0.2)

		# temp substitute for limit switch. Command lasts 0.3s
		self.setTimeout(0.3)

	def execute(self):
		return None

	def isFinished(self):
		return self.isTimedOut()

	def end(self):
		# stop arm ctre motors at end of movement
		self.robot_arm.arm_motors.left_arm_motor.stopMotor()
		self.robot_arm.arm_motors.right_arm_motor.stopMotor()

	def interrupted(self):
		self.end()

