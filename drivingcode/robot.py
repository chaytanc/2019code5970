# vim: set sw=4 sts=4 fileencoding=utf-8:
#!/usr/bin/env python3

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

#here = os.path.dirname(os.path.realpath(__file__))
#Linux RobotPyModules path
sys.path.append('./robot_py_modules') 
#Windows RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2019code5970/drivingcode/robot_py_modules') 

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

# These were commented because initializing variables outside the 
# BeaverTronicsRobot class fails with the wpilib loop thing 
# (which runs at the bottom).
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

class BeaverTronicsRobot(wpilib.IterativeRobot): 

    def robotInit(self):
    
        #Initialize Joystick Drive[steering] controls
        self.throttle = wpilib.Joystick(0)
        self.steering = wpilib.Joystick(1)

        ### Is this for Arcade? Steering and throttle aren't separate on tank
        #Initialize Joystick Pneumatic[pistons] controls
        #pn_button_L = JoystickButton(self.steering, 1)
        #pn_button_R = JoystickButton(self.throttle, 1)

        #Initialize Joystick Shifter controls
        pop = JoystickButton(self.steering, 5)#Y

        #Initialize Xbox controls (unused?)
        #xbox = wpilib.XboxController(4)
        #self.throttle = wpilib.XboxController(4) 
       
        #self.steering = wpilib.XboxController(4)
        #pop = JoystickButton(xbox, 3)
        #pop = JoystickButton(xbox, 3)#Y
    
        #experimental constants for PID equation to be tuned
        self.kp = 1.0 
        self.ki = 1.0
        self.kd = 1.0
        
        #PID equation variables
        current_velocity_left = 0.0
        current_velocity_right = 0.0
        
        #set threshold velocity error for accumulating integral values
        self.integral_value_filter = 100.0 
        
        self.error_total_left = 0.0
        self.error_total_right = 0.0
        
        self.error_previous_left = 0.0
        self.error_previous_right = 0.0
        
        proportion_left = 0.0
        proportion_right = 0.0
        integral_left = 0.0
        integral_right = 0.0
        derivative_left = 0.0
        derivative_right = 0.0
        '''
        #guillotine_motor module variables
        self.Gteen_motor = []
        self.Gteen_motor.append(wpilib.VictorSP(8))
        
        self.Gteencont = wpilib.Joystick(2)
        self.Gcoder = wpilib.Encoder(4,5)
        
        #climber_intake_winch module variables
        self.UpIntakeWinch = JoystickButton(self.Gteencont, 5)

        self.IntakeWinch_motor = []
        self.IntakeWinch_motor.append(wpilib.VictorSP(9))
                
        self.ClimberWinch = JoystickButton(self.Gteencont, 1)
        
        self.ClimberWinch_motor = []
        self.ClimberWinch_motor.append(wpilib.Spark(6))
        self.ClimberWinch_motor = []
        self.ClimberWinch_motor.append(wpilib.Spark(7))
        '''
        
        """
        This function is called upon program startup and
        should be used for any initialization code.
        """
        
        #*************************Modules******************************


        #TeleOP instances of classes
        self.winch = Winch()
        self.gteen = GteenMotor()
        self.intake = CubeIntake()
        self.pn = Pneuma()
        self.shifters = ShiftGears()
        self.encoders = Encoders()
        self.left = Left_Motors()
        self.right = Right_Motors()
        
        
        #Autonomous 
        self.automvmnt = AutoMovement()
        self.autovsn = AutoVision()

    def setDriveMotors(self, leftspeed, rightspeed):
        for motor in self.right.right_motors:
            # One of these should be positive
            motor.set(leftspeed*-1)
        for motor in self.left.left_motors:
            motor.set(rightspeed*-1)
            
    def autonomousInit(self):
        """This function is run once each time the robot enters autonomous mode."""
        #self.Lcoder = self.encoders.Lcoder
        #self.Rcoder = self.encoders.Rcoder
        #self.Gcoder = self.encoders.Gcoder
        # Declaring and Using "Lcoder", "Rcoder", and "Gcoder" leads to 
		# name errors on lines 223 and 225, where "Lcoder is not defined"
        
        self.auto_loop_counter = 0
        self.encoders.Lcoder.reset()
        self.encoders.Rcoder.reset()
        self.encoders.Gcoder.reset()
        self.stage = 0
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
        
    def autonomousPeriodic(self):
   
        print("auto_loop_counter: ")
        print(self.auto_loop_counter)
        ### The loop counter doesn't count the time, 
		# it counts iterations through autonomousPeriodic.??
        if self.auto_loop_counter < 300:
            self.setDriveMotors(-.25, .25)
            
			# error_left = current left velocity - target left velocity
            self.error_left = abs(self.encoders.Lcoder.get()) - 100 
            # target velocity will be determined based on gear box ratio 
			# and conversions of whatever units its in to whatever we want

			# error_right = current right velocity - target right velocity
            self.error_right = abs(self.encoders.Rcoder.get()) - 100 
                
            # define threshold for accumulating total error
            if self.error_left < self.integral_value_filter \
and self.error_left != 0:
                self.error_total_left += self.error_left
            else:
                self.error_total_left = 0
                    
            if self.error_right < self.integral_value_filter \
and self.error_right != 0:
                self.error_total_right += self.error_right
            else:
                self.error_total_right = 0
                    
                    
            # set maximum value for total error
            if self.error_total_left > 50/self.ki:
                self.error_total_left = 50/self.ki
                
            if self.error_total_right > 50/self.ki:
                self.error_total_right = 50/self.ki
                
                
            # derivative value becomes 0 when target velocity is reached
            if self.error_left == 0:
                derivative_left = 0
                
            if self.error_right == 0:
                derivative_right = 0
                    
            # variables for PID equation
            proportion_left = self.error_left * self.kp
            proportion_right = self.error_right * self.kp
            integral_left = self.error_total_left * self.ki
            integral_right = self.error_total_right * self.ki
            derivative_left = (self.error_left - self.error_previous_left) \
* self.kd
            derivative_right = (self.error_right - self.error_previous_right) \
* self.kd
                
                
            # set current error as previous error for next loop
            self.error_previous_left = self.error_left
            self.error_previous_right = self.error_right
                
            #PID equation:
            # set velocity to sum of "error between current and target velocity"
			#  "sum of previous errors within threshold" and "change in error"
            current_velocity_left = (proportion_left + 
				integral_left + derivative_left)
            current_velocity_right = (proportion_right + 
				integral_right + derivative_right)
                
            # INSERT IF STATEMENT TO SET current_velocity_left AND 
			# current_velocity_right TO 0 WHEN POWER IS OFF
                
            # ensure motor speed never set to negative value
            if current_velocity_left < 0:
                current_velocity_left = 0
                
            if current_velocity_right < 0:
                current_velocity_right = 0
                
            # set motor speed to PID calculated values
            self.setDriveMotors(current_velocity_left, current_velocity_right)
                
            time.sleep(0.2)
          
        else:
            self.setDriveMotors(0, 0)
        self.auto_loop_counter +=1
        data = wpilib.DriverStation.getInstance().getGameSpecificMessage()
		### Test these, see what it does, determine if necessary
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
	#driving motors
        self.drivetrainMotorControl()
	#intake/outake
        self.intake.InCube()
	#shifters
        self.shifters.Pop() 
	#raise and lower Gteen
        self.gteen.Gteen()
	#raise and lower intake
        self.winch.updown_intake()
        self.pn.pistons()
        self.winch.climber_func()
        #print("left encoder value: "+str(self.Lcoder.get()))
        #print("right encoder value: "+str(self.Rcoder.get()))
    
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
