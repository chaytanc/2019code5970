import wpilib
from wpilib.command import Subsystem
from wpilib import InterruptableSensorBase

class Arm_Switch_Front(InterruptableSensorBase):
    """
    Collect events from the front limit switch of the arm.
    """
    def __init__(self):
        super().__init__()
        # Front limit switch
        self.switch = wpilib.DigitalInput(7)
