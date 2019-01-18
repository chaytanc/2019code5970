#!/usr/bin/env python3
# vim: set sw=4 sts=4 fileencoding=utf-8:

# Robotics specifc libraries
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import drive
import time
from networktables import NetworkTables

# Non robot specific libraries
#import os
import sys
import math

#Linux RobotPyModules path
sys.path.append('./robot_py_modules') 
#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/\
robot_py_modules') 

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season

#Functions for autonomous movement of drivetrain (moving, turning, etc.)
from autonomous_movement import AutoMovement    
#Control vision for better autonomous movement [DISABLED]
from autonomous_vision import AutoVision      
#Control winches for climber & intake
from winch import Winch    
#Control 2017 guillotine motor
from guillotine_motor import GteenMotor       
#Control intake motors & pistons
from intake import CubeIntake                  
#Initialize pneumatics
from pneumatics import Pneuma              
#Control shifters
from shifter import ShiftGears                 
#Import controls
from controller import Controller               
# Encoders
from encoders import Encoders
# Motors
from left_motors import Left_Motors
from right_motors import Right_Motors

class BeaverTronicsRobot(wpilib.IterativeRobot): 

    def robotInit(self):

        #TeleOP instances of classes
        self.pn = Pneuma()
        self.encoders = Encoders()
        self.left = Left_Motors()
        self.right = Right_Motors()
        
        #Autonomous modules

	# Joystick buttons, when pressed do some function in other files
            
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
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
	    ### now diff file set_drive_motors()
	    # set drive motors to zero if auto counter is done

        self.auto_loop_counter +=1
	# Why is this necessary?
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()

    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
	# set speed of motors based on joysticks
	teleop_motor_control.py
	#intake/outakes
	#shifters
	# any lineup code used for teleop 
    
    def testPeriodic(self):
        """This function is called periodically during test mode."""
    
if __name__ == "__main__":
    wpilib.run(BeaverTronicsRobot)
