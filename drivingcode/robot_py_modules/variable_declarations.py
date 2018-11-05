import wpilib
from wpilib.buttons.joystickbutton import JoystickButton


'''
Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 
'''


class VariableDec():
    #**************Robot-Side Initialization***************        
    #Initialize ClimberIntakeWinch motors
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
                
    #***************Driverstation Initialization******************
                
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
            
     