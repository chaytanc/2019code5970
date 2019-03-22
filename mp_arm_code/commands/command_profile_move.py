# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import CommandGroup

from do_profile_move import Do_Profile_Move

class Command_Profile_Move(CommandGroup):
    def __init__(self, robot):
        super().__init__()
        #self.addSequential(Do_Generate_Profile(robot))
        #XXX setpoint needs to be updated IN moving the arm pid because
        # getting the setpoint is a function, not a command and thus
        # does not work with sequential commands
        self.addSequential(Do_Profile_Move(robot, 25))

