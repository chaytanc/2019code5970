import wpilib
from wpilib.command import Command

class Do_Arm_Test(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.arm = robot.arm

    def execute(self):
        self.arm.set_motors(0.5)

