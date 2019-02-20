import wpilib
from wpilib.command import InstantCommand

class Do_Zero_Encoder(InstantCommand):
    def __init__(self, robot):
        super().__init__()

        self.robot = robot
        #XXX Don't want it to interrupt the arm because then it will never get
        # off the limit switch after zeroing because it will constantly
        # interrupt and set to zero.
        #self.requires(self.robot.arm)
        self.encoder = self.robot.arm.l_arm_encoder

    def initialize(self):
        # Zeroes arm encoder
        #XXX if not using requestinterrupts
        if self.robot.b_limit.get():
            self.encoder.reset()

    def execute(self):
        return None

    def end(self):
        return None

    def interrupted(self):
        return None

    def isInterruptible(self):
        return False

