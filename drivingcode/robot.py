#!/usr/bin/env python3
import wpilib
import math
from wpilib.buttons.joystickbutton import JoystickButton
import drive

#import os
import sys

#here = os.path.dirname(os.path.realpath(__file__))
#sys.path.append('./RobotPyModules/Pneumatics') #Linux RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules') #Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules/add-ons') #Windows RobotPyModules path

#from variable_declarations import VariableDec   #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

import autonomous_movement     #Functions for autonomous movement of drivetrain (moving, turning, etc.)
import autonomous_vision       #Control vision for better autonomous movement [DISABLED]

import climber_intake_winch    #Control winches for climber & intake
import guillotine_motor        #Control 2017 guillotine motor
import intake                  #Control intake motors & pistons
import pneumatics              #Initialize pneumatics
import shifter                 #Control shifters
'''
Test assertion error possible related to variabledec
'''

class BeaverTronicsRobot( wpilib.IterativeRobot): #VariableDec,
    def robotInit(self):
    
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        
        #*************************Modules******************************
        
        #TeleOP modules
        self.clmbr = climber_intake_winch.Winch()
        self.gtn = guillotine_motor.GteenMotor()
        self.intk = intake.CubeIntake()
        self.pn = pneumatics.Pneuma()
        self.shftrs = shifter.ShiftGears()
        
        #Autonomous 
        self.automvmnt = autonomous_movement.AutoMovement()
        self.autovsn = autonomous_vision.AutoVision()
        
        
    def wrist(self,state):#must get maximum and minimum
        max_wrist=90#set low so it will stop before it breaks itself at 100
        min_wrist=10#set high so it will stop before it breaks itself at 0
        if direction =="Forward":
            while self.Wcoder.get()<max_wrist:
                for motor in self.CubeIntakeL_motor:
                    motor.set(.25)
            for motor in self.CubeIntakeL_motor:
                    motor.set(0)
        elif direction =="Backward":
            while self.Wcoder.get()<max_wrist:
                for motor in self.CubeIntakeL_motor:
                    motor.set(-.25)
            for motor in self.CubeIntakeL_motor:
                    motor.set(0)

    def setDriveMotors(self, leftspeed, rightspeed):
        for motor in self.right_motors:
            motor.set(leftspeed*-1)
        for motor in self.left_motors:
            motor.set(rightspeed*-1)
            
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        self.auto_loop_counter = 0
        self.Lcoder.reset()
        #self.Rcoder.reset()
        self.Gcoder.reset()
        self.stage = 0
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        
    def autonomousPeriodic(self):
        print("got to 288")
        if self.auto_loop_counter < 300:
            self.setDriveMotors(-.25, .25)
        else:
            self.setDriveMotors(0, 0)
        self.auto_loop_counter = self.auto_loop_counter+1
        #data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        #self.automvmnt.drive_forward(5000,'Backward')
        #self.setDriveMotors(.10,.10)
        #if data.find("R",0,0) == 0:
            #self.automvmnt.turn(180)
        #self.degrees, self.azim, self.distance=self.autovsn.find_tape()
        #self.automvmnt.turn(self.degrees)
        #self.automvmnt.drive_forward(self.distance,'Forward') 
        #elif data.find("L",0,0) == 0:
            #self.stage=1000
            #self.automvmnt.drive_forward(7000,'Forward')
            #self.automvmnt.turn(-90)
            #self.automvmnt.drive_forward(10000,'Forward')
            #self.automvmnt.turn(-90)
            #self.degrees, self.azim, self.distance=self.autovsn.find_tape()
            #self.automvmnt.turn(self.degrees)
            #self.automvmnt.drive_forward(self.distance,'Forward')
        #else:
            #self.automvmnt.drive_forward(7000,'Forward')
            
    def teleopPeriodic(self):
        """This function is called periodically during operator control."""
        self.drivetrainMotorControl()#driving motors
        #self.intk.InCube()#intake/outake
        self.shftrs.Pop() #shifters
        self.gtn.Gteen()#raise and lower Gteen
        self.clmbr.UpDownIntake()#raise and lower intake
        self.pn.pistons()
        self.clmbr.Climber()
        print("left encoder value "+str(self.Lcoder.get()))
        #print("right encoder value "+str(self.Rcoder.get()))
    
    def testPeriodic(self):
        """This function is called periodically during test mode."""
    
    def drivetrainMotorControl(self):
        #xbox drivetrainMotorControl definitions
        #left = self.xbox.getRawAxis(5)
        #right = self.xbox.getRawAxis(1)
        
        left = self.throttle.getY()
        right = self.steering.getY()
        
        drive_powers = drive.tankdrive(right*-1, left*-1)
        self.leftspeeds = drive_powers[0]
        self.rightspeeds = drive_powers[1]
        # set the motors to powers
        self.setDriveMotors(self.leftspeeds, self.rightspeeds)
               
if __name__ == "__main__":
    wpilib.run(BeaverTronicsRobot)
