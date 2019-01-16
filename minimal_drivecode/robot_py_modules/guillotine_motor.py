# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2019/code5970/drivingcode/robot_py_modules')

#from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

class GteenMotor():
#*********Robot-Side Initialization***************
    def __init__(self):
        #Initialize GteenMotorControl
        self.Gteen_motor = []
        self.Gteen_motor.append(wpilib.VictorSP(8))
        
        self.Gteencont = wpilib.Joystick(2)
        self.Gcoder = wpilib.Encoder(4,5)
    '''
    Control autonomous turns?
    '''
        
    def Gteen(self):
        value = self.Gteencont.getY()#405 is the desired max on practice bot
        turning = self.Gcoder.get()#405 is the desired max
        '''
        if -1*value <= 0:
            print("falling at "+str(value))
            if turning >= 300:
                for motor in self.Gteen_motor:
                    motor.set(-.05)#fall fast
            elif turning >= 200:
                for motor in self.Gteen_motor:
                    motor.set(-.05)#fall medium
            elif turning >= 10:
                for motor in self.Gteen_motor:
                    motor.set(-.05)#fall 
            elif turning >= 5:
                for motor in self.Gteen_motor:
                    motor.set(0)
                    
                    
                    #fall slow
            #check if its high up or low up
            # if top 2% then fall fast(because it should be resting set output to 0)
            
            
        elif -1*value > .25:
            print("rising at "+str(value))
            if turning <= 100:
                for motor in self.Gteen_motor:
                    motor.set(-.8)#rise fast
            elif turning <= 200:
                for motor in self.Gteen_motor:
                    motor.set(-.6)#rise medium
            elif turning <= 380:
                for motor in self.Gteen_motor:
                    motor.set(-.6)#rise slow 
            elif turning <= 400:
                for motor in self.Gteen_motor:
                    motor.set(-0.3)
        else:
            for motor in self.Gteen_motor:
                motor.set(-0.3)'''
        
        print("The G encoder is at: "+str(turning))
        for motor in self.Gteen_motor:
            motor.set(value)
        print("the value for the motor power "+str(value))
      
