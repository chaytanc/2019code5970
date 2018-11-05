import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class ShiftGears(VariableDec):
    '''
    Control shifters
    '''
        
    def Pop(self):
        if self.pop.get():
            self.shiftL.set(True)
            self.shiftR.set(True)
            #for motor in self.pop_motor:
                #motor.set(1)
        else:
            self.shiftL.set(False)
            self.shiftR.set(False)
            #for motor in self.pop_motor:
                #motor.set(0)
                
        