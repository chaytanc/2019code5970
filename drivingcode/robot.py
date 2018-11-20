#!/usr/bin/env python3

# Robotics specifc libraries
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import drive

# Non robot specific libraries
#import os
import sys
import math

#here = os.path.dirname(os.path.realpath(__file__))
#Linux RobotPyModules path
#sys.path.append('./RobotPyModules/Pneumatics') 
#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules') 
#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules/add-ons') 

# Subsidiary objects on the robot. Ex: Cube Intake from 2017/18 season
from left_motors import Left_Motors
from right_motors import Right_Motors
from autonomous_movement import AutoMovement     #Functions for autonomous movement of drivetrain (moving, turning, etc.)
from autonomous_vision import AutoVision      #Control vision for better autonomous movement [DISABLED]
from winch import Winch    #Control winches for climber & intake
from guillotine_motor import GTeenMotor       #Control 2017 guillotine motor
from intake import CubeIntake                  #Control intake motors & pistons
from pneumatics import Pneuma              #Initialize pneumatics
from shifter import ShiftGears                 #Control shifters
from controller import Controller               #Import controls


'''
Test assertion error possible related to variabledec
'''

'''
ClimberWinch_motor = []
ClimberWinch_motor.append(wpilib.Spark(6))
ClimberWinch_motor = []
ClimberWinch_motor.append(wpilib.Spark(7))

IntakeWinch_motor = []
IntakeWinch_motor.append(wpilib.VictorSP(9))

#Initialize Drive motors
left_motors = []
left_motors.append(wpilib.VictorSP(0))
left_motors.append(wpilib.VictorSP(1))
left_motors.append(wpilib.VictorSP(2))#2

right_motors = []
right_motors.append(wpilib.VictorSP(4))#4
right_motors.append(wpilib.VictorSP(3))
right_motors.append(wpilib.VictorSP(5))

#Initialize Encoders
#Rcoder = wpilib.Encoder(2,3)
Lcoder = wpilib.Encoder(0,1)
Gcoder = wpilib.Encoder(4,5)
Wcoder = wpilib.Encoder(2,3)

#Initialize GteenMotorControl motors
Gteen_motor = []
Gteen_motor.append(wpilib.VictorSP(8))

#Initialize Intake motors (missing?)
#CubeIntakeL_motor = []
#CubeIntakeR_motor = []

#Initialize Pneumatics[pistons]
pistonL = wpilib.Solenoid(2)
pistonR = wpilib.Solenoid(3)

#Initialize Shifter
shiftL = wpilib.Solenoid(0)
shiftR = wpilib.Solenoid(1)

#Initialize Shifter[pop motors]
#pop_motor = []
#pop_motor.append(wpilib.VictorSP(7))

#Initialize Ultrasonic sensors
#Ultra = wpilib.AnalogInput(3)
Gyroo = wpilib.ADXRS450_Gyro()
'''

#***************Driverstation Initialization******************
### THIS IS PROBABLY VERY MESSED UP DUE TO NAMING CHANGES

#Initialize Joystick Drive[steering] controls
throttle = wpilib.Joystick(0)
steering = wpilib.Joystick(1)
Gteencont = wpilib.Joystick(2)

#Initialize Joystick ClimberIntakeWinch controls
UpIntakeWinch = JoystickButton(Gteencont, 5)
DownIntakeWinch = JoystickButton(Gteencont, 6)
ClimberWinch = JoystickButton(Gteencont, 1)

#Initialize Joystick Intake controls
CubeIntakeUp1 = JoystickButton(Gteencont,3)
#CubeIntakeDown1 = JoystickButton(Gteencont, 4)
CubeIntakeUp2 =JoystickButton(throttle,3)
#CubeIntakeDown2 =JoystickButton(throttle,4)

#Initialize Joystick Pneumatic[pistons] controls
pn_button_L = JoystickButton(steering, 1)
pn_button_R = JoystickButton(throttle, 1)

#Initialize Joystick Shifter controls
pop = JoystickButton(steering, 5)#Y



#Initialize Xbox controls (unused?)
xbox = wpilib.XboxController(4)
#throttle = wpilib.XboxController(4)
#steering = wpilib.XboxController(4)
        pop = JoystickButton(xbox, 3)
        #pop = JoystickButton(xbox, 3)#Y

class BeaverTronicsRobot(wpilib.IterativeRobot): #VariableDec,
    def robotInit(self):
    
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        
        #*************************Modules******************************


        #TeleOP modules
        self.winch = Winch()
        self.gtn = GteenMotor()
        self.intk = CubeIntake()
        self.pn = Pneuma()
        self.shftrs = ShiftGears()
        
        #Autonomous 
        self.automvmnt = AutoMovement()
        self.autovsn = AutoVision()



        
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
        #Each iteration may create new class; add if statements to fix?
        """This function is called periodically during operator control."""
        self.drivetrainMotorControl()#driving motors
        #self.intk.InCube()#intake/outake
        self.shftrs.Pop() #shifters
        self.gtn.Gteen()#raise and lower Gteen
        self.winch.updown_intake()#raise and lower intake
        self.pn.pistons()
        self.winch.climber_func()
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
    self.vrbls.VariableList()