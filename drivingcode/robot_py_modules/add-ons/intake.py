import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys

sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/RobotPyModules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class CubeIntake(VariableDec):
    '''
    Control intake motors & pistons
    '''
    
    def InCube(self):#intake function
        if self.CubeIntakeUp1.get() or self.CubeIntakeUp2.get():
            for motor in self.CubeIntakeL_motor:
                motor.set(2.003)
            for motor in self.CubeIntakeR_motor:
                motor.set(-2.003)
        #elif self.CubeIntakeDown1.get() or self.CubeIntakeDown2.get():
            #for motor in self.CubeIntakeL_motor:
                #motor.set(-2.003)
            #for motor in self.CubeIntakeR_motor:
                #motor.set(2.003)
        else:
            for motor in self.CubeIntakeL_motor:
                motor.set(0)
            for motor in self.CubeIntakeR_motor:
                motor.set(0)
                
    def pinser(self,state):
        self.auto_loop_counter = 0
        while self.auto_loop_counter <= 50:
            self.pistonL.set(False)
            self.pistonR.set(False)
            self.auto_loop_counter= self.auto_loop_counter+1
        self.pistonL.set(True)
        self.pistonR.set(True)
        return 0
        
    def AutoInCube(self,what):#autonomous intake function
        if self.CubeIntakeUp1.get():
            if what == 1:
                for motor in self.CubeIntakeL_motor:
                    motor.set(1)
                for motor in self.CubeIntakeR_motor:
                    motor.set(1)
            else:
                for motor in self.CubeIntakeL_motor:
                    motor.set(0)
                for motor in self.CubeIntakeR_motor:
                    motor.set(0)