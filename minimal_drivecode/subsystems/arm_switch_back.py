import wpilib
from wpilib.command import Subsystem
from wpilib import InterruptableSensorBase

#class Arm_Switch_Back(InterruptableSensorBase):
class Arm_Switch_Back(Subsystem):
    """
    Collect events from the back limit switch of the arm.
    """
    def __init__(self):
        super().__init__()
        # Back limit switch of arm
        self.switch = wpilib.DigitalInput(8)
        self.counter = wpilib.Counter(self.switch)
        self.counter.reset()
        #self.getAnalogTriggerTypeForRouting()
        #self.getPortHandleForRouting()
        #print(self.getAnalogTriggerTypeForRouting())
        #print(self.getPortHandleForRouting())

    def check_counter(self):
        self.hit_limit = (self.counter.get() > 0)
        return self.hit_limit 

    def init_counter(self):
        self.counter.reset()
