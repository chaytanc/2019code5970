# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

class Do_Arm_Interrupt(Command):

    def __init__(self, robot):
        super().__init__()
        self.requires(robot.arm)
        self.robot_arm = robot.arm

    def initialize(self):
        print("Ran Command Do_Arm_Interrupt")
        return None

    def execute(self):
       self.robot_arm.set_motors(0) 

    def isFinished(self):
        return None

    def end(self):
        return None

    def interrupted(self):
        self.end()
