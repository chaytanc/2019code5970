#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
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
		self.drivetrain = Drivetrain(self)

		# OI
		self.oi = OI(self)
		
	def autonomousInit(self):
		# Set up encoders
		# Loop counter to stop/start auto?
		# Reset encoders (zero them) upon init
		# Get Driverstation data from field
		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		# Initialize pid variables
		
	def autonomousPeriodic(self):
		###Commented out temporarily
		#pid_loop.do_pid_loop()
		return None

	def teleopPeriodic(self):
	# Before, button functions were executed here. Now scheduler will do that
		Scheduler.getInstance().run()
	
	def testPeriodic(self):
		return None

	def disabledInit(self):
		return None
	
	def disabledPeriodic(self):
		return None

	def robotPeriodic(self):
		return None
	
if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
