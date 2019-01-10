# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys

sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/RobotPyModules')


class CubeIntake():
    #*********Robot-Side Initialization***************
    def __init__(self):
        #Initialize Intake motors (missing?)
        self.CubeIntakeL_motor = []
        self.CubeIntakeR_motor = []
        
        self.throttle = wpilib.Joystick(0)
        Gteencont = wpilib.Joystick(2)

        #Initialize Joystick ClimberIntakeWinch controls
        UpIntakeWinch = JoystickButton(Gteencont, 5)
        DownIntakeWinch = JoystickButton(Gteencont, 6)
        ClimberWinch = JoystickButton(Gteencont, 1)
        
        #Initialize Joystick Intake controls
        self.CubeIntakeUp1 = JoystickButton(Gteencont,3)
        #self.CubeIntakeDown1 = JoystickButton(Gteencont, 4)
        self.CubeIntakeUp2 =JoystickButton(self.throttle,3)
        #self.CubeIntakeDown2 =JoystickButton(self.throttle,4)
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
                
	### Should this be in autonomous movement
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
