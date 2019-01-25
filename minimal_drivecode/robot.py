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
#from pneumatics import Pneuma			  
#from encoders import Encoders
###
#import left_motors as lm
#import right_motors as rm
###
from left_motors import Left_Motors
from right_motors import Right_Motors
#import arm_motors as am
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
		#am = am.Arm_Motors()
		#left_intake = am.left_intake
		#right_intake = am.right_intake
		
		# Modules
		#self.pn = Pneuma()
		#self.encoders = Encoders()
		#self.arm = arm.Arm()
		

		# Autonomous modules

		# Tank Drive mode
		self.lj = js.My_Joystick(0)
		self.rj = js.My_Joystick(1)

		self.drive = tank.set_tank_drive(left_motors, right_motors)

		# Joystick buttons, when pressed do some function in other files
#		cargo_eject_butt = js.set_button(self.lj, 0)
#		ramp_deploy_butt = js.set_button(self.lj, 1)
#		ramp_up_butt = js.set_button(self.lj, 2)
#
#		hp_eject_butt = js.set_button(self.rj, 0)
#		lineup_butt = js.set_button(self.rj, 4)
#		highgear_butt = js.set_button(self.lj, 4)
		
		
		
			
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
		if self.auto_loop_counter < 300:
			self.setDriveMotors(-.25, .25)
			
			# Get inputs for PID
				
			# PID loop for target velocity on each side of drivetrain in auto
			# Input: target pathway (Noah code)
			pid = Pid_Loop()	
			previous_error = self.error 
			self.error = pid.get_error()
			self.total_error = pid.set_total_error(self.error, self.total_error)
			proportion = pid.set_proportion()
			max_error = pid.set_max_error()
			integral = pid.set_integral()
			derivative = pid.set_derivative(self.error, self.kd, previous_error)
			###right_velocity = pid.get_velocity()
					
			# Outputs for PID
		
				# set motor speed to PID outputs 
	
			time.sleep(0.2)
		  
		else:
			# set drive motors to zero if auto counter is done
	
			self.auto_loop_counter +=1
			# Why is this necessary?
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
