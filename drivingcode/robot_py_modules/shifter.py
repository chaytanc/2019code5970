import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')


class ShiftGears():
    #*********Robot-Side Initialization***************
    def __init__(self):
            #Initialize Shifter
            shiftL = wpilib.Solenoid(0)
            shiftR = wpilib.Solenoid(1)
            
            #Initialize Shifter[pop motors]
            #pop_motor = []
            #pop_motor.append(wpilib.VictorSP(7))
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
                
        