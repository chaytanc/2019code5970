# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from sys import path
path.append('../')
# commands used in commandgroup
from do_cargo_eject import Do_Cargo_Eject
from do_move_arm import Do_Move_Arm

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Command_Cargo_Eject(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses motor 6 and ctre motors 1 & 2
		
		# Cargo can only be in two states:
		#	1: rotating inwards with Arm at front of robot
		#	2: rotating outwards with Arm at back of robot

		# state 2

		#self.addSequential(Do_Move_Arm(robot, 100))
		self.addSequential(Do_Cargo_Eject(robot))


