# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from sys import path
path.append('../')
# commands used in commandgroup
from do_ramp import Do_Ramp
from do_move_arm import Do_Move_Arm

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Command_Ramp(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses solenoids 5 and ctre motors 1 & 2
		
		# Ramp can only be in one state:
		#	1: actuated with Arm at ????

		# state 1

		# temporary Move_Arm angle of 100.
		# BEING WEIRD
		#self.addSequential(Do_Move_Arm(robot, 100))
		self.addSequential(Do_Ramp(robot))

