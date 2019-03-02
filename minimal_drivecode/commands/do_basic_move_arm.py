# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# positions Arm to robot back for calibrating autonomous
class Do_Basic_Move_Arm(Command):
	def __init__(self, robot):
		super().__init__()

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
		self.robot_arm.arm_motors.left_arm_motor.set(-0.2)
		self.robot_arm.arm_motors.right_arm_motor.set(-0.2)

		# temp substitute for limit switch. Command lasts 0.3s
		self.setTimeout(0.3)

	def execute(self):
		return None

	def isFinished(self):
		return self.isTimedOut()

	def end(self):
		# stop arm ctre motors at end of command
		self.robot_arm.arm_motors.left_arm_motor.stopMotor()
		self.robot_arm.arm_motors.right_arm_motor.stopMotor()

	def interrupted(self):
		print("Command 'basic_move_arm' interrupted!")
		self.end()

