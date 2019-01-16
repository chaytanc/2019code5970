# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton



class Controller():
 #***************Driverstation Initialization******************
    def __init__(self):
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
            
