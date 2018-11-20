import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')
    

class Winch():
    def __init__(self):
     #Initialize ClimberIntakeWinch motors
        ClimberWinch_motor = []
        ClimberWinch_motor.append(wpilib.Spark(6))
        ClimberWinch_motor = []
        ClimberWinch_motor.append(wpilib.Spark(7))
        IntakeWinch_motor = []
        IntakeWinch_motor.append(wpilib.VictorSP(9))
    '''
    Control winches for climber & intake
    '''
    def updown_intake(self):#intake winch function
        if self.UpIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(0.25)
        elif self.DownIntakeWinch.get():
            for motor in self.IntakeWinch_motor:
                motor.set(-0.25)
        else:
            for motor in self.IntakeWinch_motor:
                motor.set(0)
                
    def climber_func(self):#Climber winch function
        if self.ClimberWinch.get():
            for motor in self.ClimberWinch_motor:
                motor.set(0.25)
        else:
            for motor in self.ClimberWinch_motor:
                motor.set(0)
   