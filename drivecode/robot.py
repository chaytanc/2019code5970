#!/usr/bin/env python3
# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.command import Scheduler
# for Automous Scheduler
# from commands.autonomous import Autonomous
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

#RoboRIO path
sys.path.insert(0, '/home/lvuser/py/subsystems')
sys.path.insert(0, '/home/lvuser/py/commands')

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from arm_motors import Arm_Motors
from left_motors import Left_Motors
from right_motors import Right_Motors

from drivetrain import Drivetrain
from hp_intake import Hp_Intake
from ramp import Ramp
from shifters import Shifters

# Limit switches
#from back_switch import Back_Switch

# Teleop init command
#from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig

from oi import OI

class BeaverTronicsRobot(wpilib.TimedRobot): 

	def robotInit(self):
		# Instances of classes

		# Instantiate Subsystems
		self.drivetrain = Drivetrain(self)
		self.hp_intake = Hp_Intake()
		self.ramp = Ramp()
		self.shifters = Shifters()

		# instantiate Encoders for drivetrain?
		#self.encoders = Encoders(self)

		# Instantiate Joysticks
		self.left_joy = wpilib.Joystick(0) 
		self.right_joy = wpilib.Joystick(1)
		
		# Instantiate Xbox
		self.xbox = wpilib.Joystick(2)

		# Instantiate OI; must be AFTER joysticks are inited
		self.oi = OI(self)

		self.timer = wpilib.Timer()
		self.loops = 0

		# slightly untested vision
		wpilib.CameraServer.launch("vision.py:main")
		
		
		
	def autonomousInit(self):
		Scheduler.getInstance().removeAll()
		# Set up encoders
		# Loop counter to stop/start auto?
		# Get Driverstation data from field

		data = wpilib.DriverStation.getInstance().getGameSpecificMessage()

		# Autonomous Scheduler
		# self.autonomousCommand.start()
		
	def autonomousPeriodic(self):
		#XXX hatch panel
		Scheduler.getInstance().run()
		#return None

	def teleopInit(self):
		self.loops = 0
		self.timer.reset()
		self.timer.start()

		Scheduler.getInstance().removeAll()
		Scheduler.getInstance().enable()

	def teleopPeriodic(self):

	# Before, button functions were executed here. Now scheduler will do that
	
		Scheduler.getInstance().run()

		# Keeping track of TimedRobot loops through code
		self.loops += 1
		if self.timer.hasPeriodPassed(1):
			self.logger.info("%d loops / second", self.loops)
			self.loops = 0

	def disabledInit(self):
		# remove all commands from scheduler
		#self.arm_motors.set_speed(0, False)
		Scheduler.getInstance().removeAll()
		
		return None

	def disabledPeriodic(self):
		return None

	
if __name__ == "__main__":
	wpilib.run(BeaverTronicsRobot)
