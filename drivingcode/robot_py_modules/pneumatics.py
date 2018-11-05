import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class Pneuma(VariableDec):
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
    
    