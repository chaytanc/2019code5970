import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class Winch(VariableDec):
    '''
    Control winches for climber & intake
    '''
    def UpDownIntake(self):#intake winch function
        if self.UpIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(0.25)
        elif self.DownIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(-0.25)
        else:
            for motor in self.IntakeWinch_motor:
                motor.set(0)
                
    def Climber(self):#Climber winch function
        if self.ClimberWinch.get():
            for motor in self.ClimberWinch_motor:
                motor.set(0.25)
        else:
            for motor in self.ClimberWinch_motor:
                motor.set(0)
   