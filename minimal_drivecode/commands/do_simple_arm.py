# vim: set sw=4 noet ts=4 fileencoding=utf-8:
from wpilib.command import Command
import wpilib

class Do_Simple_Arm(Command):
    
    def __init__(self, robot):
        self.arm_motors = robot.arm.arm_motors

    def initialize(self):
        return None

    def execute(self):
        self.arm_motors.set_speed(0.1)

    def isFinished(self):
        return None

    def end(self):
        self.arm_motors.set_speed(0)

    def interrupted(self):
        self.end()

    def isInterruptible(self):
        return True
