import wpilib
from wpilib.command import InstantCommand

class Do_Recal_Clicks(InstantCommand):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(self.robot.arm)

    def initialize(self):
        self.robot.arm.set_rel_clicks()

    def execute(self):
        return None

    def end(self):
        self.robot.arm.set_motors(0)

    def interrupted(self):
        return None

    def isInterruptible(self):
        return False

