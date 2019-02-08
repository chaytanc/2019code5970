# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.drive import DifferentialDrive
from wpilib.command import Subsystem
from left_motors import Left_Motors
from right_motors import Right_Motors
from arm_motors import Arm_Motors
from cargo_motors import Cargo_Motors
from sys import path
path.append('../commands')
from do_tank_drive import Do_Tank_Drive
import math


class Drivetrain(Subsystem):

	def __init__(self, robot):
		# Super from subsystem allows scheduler class to understand things like
		# interupt and execute etc...
		print("$$$$$$$$$$$$$$")
		super().__init__()
		print("$$$$$$$$$$$$$$")
	
		# Motors
		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		self.left_motors = left_motors_instance.left_motor_group
		self.right_motors = right_motors_instance.right_motor_group

		arm_motors_instance = Arm_Motors()
		self.left_arm_motors = arm_motors_instance.left_arm_motor
		self.right_arm_motors = arm_motors_instance.right_arm_motor

		cargo_motors_instance = Cargo_Motors()
		self.cargo_motors = cargo_motors_instance.cargo_m

		# Encoders
		self.left_drive_encoder = wpilib.Encoder(2,3)#DIO Ports??
		self.right_drive_encoder = wpilib.Encoder(4,5)#DIO Ports??
		self.arm_encoder = wpilib.Encoder(6,7)#DIO Ports??

		# Instantiate robot
		self.robot_instance = robot
	
		# Tank Drive Drivetrain
		self.drive = self.set_drivetrain_type(DifferentialDrive, 
			self.left_motors, self.right_motors)


	def initDefaultCommand(self):
		self.setDefaultCommand(Do_Tank_Drive(self.robot_instance))

	# Sets driving mode to tank drive, should be periodically called
	def set_drivetrain_type(self, drivetrain_type, left_motors, right_motors):
		# DifferentialDrive for tank
		drive = drivetrain_type(left_motors, right_motors)
		return drive

	def set_tank_speed(self, left_joy, right_joy, drive=DifferentialDrive):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		drive.tankDrive(left_speed, right_speed)
	
	def motor_test_max_speed(self):
		self.left_arm_motors.set(1)
		#self.right_arm_motors.set(-1)

	def cargo_intake_test(self, third_joy, drive=DifferentialDrive):
		third_speed = third_joy.getY()
		self.cargo_motors.set(third_speed)


	def stop_robot(self, drive):
		drive.tankDrive(0,0)
	
	def reset_encoder(self):
		self.right_encoder.reset()

	# Get encoder direction:
	def get_direction(self):
		return(self.arm_encoder.getDirection())

	# Get encoder rate:
	def get_rate(self):
		return(self.arm_encoder.getRate())

	def sin_relative_angle(self,current_angle, desired_angle):
		current_angle_radians = current_angle * math.pi/180
		desired_angle_radians = desired_angle * math.pi/180
		voltage = (math.sin((math.pi/desired_angle_radians)
				*current_angle_radians))
		return voltage
	

		
		

