import wpilib
from wpilib.command import InstantCommand

class Do_Zeroed_Clicks(InstantCommand):
    
    def __init__(self, robot):
        super().__init__()
        ''' Only called by requesting the interupts of the back limit switch
        sensor'''
        self.robot = robot
        # Will interrupt arm when used
        self.requires(self.robot.arm)

    def initialize(self):
        print("initialization of Do_Zero_Encoder command")
        self.robot.arm.set_zeroed_clicks() 

    def execute(self):
       return None

    #XXX Does this get run in an InstantCommand?
    def end(self):
        # Turn off arm motors
        self.robot.arm.set_motors(0)

    def interrupted(self):
        return None

    def isInterruptible(self):
        return False

