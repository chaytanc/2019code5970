import wpilib
from wpilib.command import Command

class Do_Arm_Go_Back(Command):
    def __init__(self, robot):
        super().__init__()
        self.robot = robot
        self.requires(robot.arm)

    def execute(self):
        self.robot.arm.arm_motors.set_speed(-7.0, False)

    #XXX
    def isFinished(self):
        return None

    def end(self):
        print("do arm go back: Ending Command")
        self.robot.arm.arm_motors.set_speed(0, False)

    def interrupted(self):
        self.end()
