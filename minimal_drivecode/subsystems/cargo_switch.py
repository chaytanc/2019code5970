import wpilib
from wpilib.command import Subsystem
from wpilib import InterruptableSensorBase

class Cargo_Switch(InterruptableSensorBase):
    """
    Collect events from the limit switch cargo loader
    """
    def __init__(self):
        super().__init__()
        # Cargo limit switches
        self.switch = wpilib.DigitalInput(9)
