# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')



class Pneuma():
    #*********Robot-Side Initialization***************
    def __init__(self):
        #Initialize Pneumatics[pistons]
        self.pistonL = wpilib.Solenoid(2)
        self.pistonR = wpilib.Solenoid(3)
        
        #Initialize Joystick Drive[steering] controls
        self.throttle = wpilib.Joystick(0)
        self.steering = wpilib.Joystick(1)
            
        #Initialize Joystick Pneumatic[pistons] controls
        self.pn_button_L = JoystickButton(self.steering, 1)
        self.pn_button_R = JoystickButton(self.throttle, 1)
    '''
    Compress air for pistons?
    '''
    def pistons(self):
        if self.pn_button_L.get():
            self.pistonL.set(False)
        else:
            self.pistonL.set(True)
        if self.pn_button_R.get():
            self.pistonR.set(False)
        else:
            self.pistonR.set(True)
    
    
