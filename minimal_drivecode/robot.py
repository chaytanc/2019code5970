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
sys.path.append('./subsystems') 
sys.path.append('./commands') 

#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
subsystems') 
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
commands') 

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from oi import OI
from drivetrain import Drivetrain
from left_motors import Left_Motors
from right_motors import Right_Motors

class BeaverTronicsRobot(wpilib.IterativeRobot): 

	def robotInit(self):

		# Instances of classes

		# Subsystems
		drivetrain = Drivetrain()

		# OI
		oi = OI()

		# Motors
		### Dunno if necessary, motors will be passed into set_speed command
		#left_motors_instance = Left_Motors()
		#right_motors_instance = Right_Motors()
		#left_motors = left_motors_instance.left_motor_group
		#right_motors = right_motors_instance.right_motor_group

		# Autonomous modules

		# Tank Drive mode
		# Joysticks are made when used in commands (namely set_speed)
		#self.lj = js.My_Joystick(0)
		#self.rj = js.My_Joystick(1)

		# Joystick buttons are no longer initialized here but in OI
		
	def autonomousInit(self):
		# Set up encoders
		# Loop counter to stop/start auto?
		# Reset encoders (zero them) upon init
		# Get Driverstation data from field
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		# Initialize pid variables
		
	def autonomousPeriodic(self):
		pid_loop.do_pid_loop()

	def teleopPeriodic(self):
	# Before, button functions were executed here. Now scheduler will do that
		Scheduler.getInstance().run()
	
	def testPeriodic(self):
		"""This function is called periodically during test mode."""
	
if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
