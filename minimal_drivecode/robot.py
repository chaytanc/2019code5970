#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import time
from networktables import NetworkTables

# Non robot specific libraries
import os
import sys
import math

#Linux path
sys.path.append('./modules') 
sys.path.append('./logic') 

#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
robot_py_modules') 
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
robot_logic') 

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/modules')
sys.path.insert(0, '/home/lvuser/py/logic')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from left_motors import Left_Motors
from right_motors import Right_Motors
import tank
import joysticks as js

class BeaverTronicsRobot(wpilib.IterativeRobot): 

	def robotInit(self):

		# Instances of classes

		# Motors
		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		left_motors = left_motors_instance.left_motor_group
		right_motors = right_motors_instance.right_motor_group
		
		# Tank Drive mode
		self.lj = wpilib.Joystick(0)
		self.rj = wpilib.Joystick(1)

		self.drive = tank.set_tank_drive(left_motors, right_motors)
		
			
	def autonomousInit(self):
		"""This function is run once each time the robot enters 
		autonomous mode."""

		# Set up encoders

		# Loop counter to stop/start auto?

		# Reset encoders (zero them) upon init
		
		# Get Driverstation data from field
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		self.error = 0
		self.total_error = 0
		
	def autonomousPeriodic(self):
   
	# Begin auto loop counter for controlling auto? Loop if less than x val
			data = wpilib.DriverStation.getInstance().getGameSpecificMessage()

	def teleopPeriodic(self):
		"""This function is called periodically during operator control."""

		# Set speed of motors based on joysticks
		tank.set_tank_speed(self.lj, self.rj, self.drive)

		# Executing button functions
		#js.do(cargo_eject_butt, arm.cargo_eject(), xxxargs) 
		#js.do(ramp_deploy_butt, arm.ramp_deploy(), xxxargs)
		### etc

		#intake/outakes
		### Test this later
		#js.do(
		#	cargo_intake_butt, arm.cargo_intake, self.intake_motor_group) 

		

		#shifters

	# any lineup code used for teleop 
	
	def testPeriodic(self):
		"""This function is called periodically during test mode."""
	
if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
