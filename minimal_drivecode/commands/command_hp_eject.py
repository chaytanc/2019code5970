# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

from sys import path
path.append('../')
# commands used in commandgroup
from do_hp_eject import Do_Hp_Eject
from do_hp_intake import Do_Hp_Intake
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated 
from do_move_arm import Do_Move_Arm

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Command_Hp_Eject(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses solenoids 3 & 4 and ctre motors 1 & 2
		
		# Hatch Panel can only be in two states:
		#	1: unactuated with Arm at back of robot. Actuates once.
		#	2: unactuated with Arm at front of robot

		# state 1

		# BEING WEIRD
		#self.addSequential(Do_Move_Arm(robot, 0))
		self.addSequential(Do_Hp_Rotate_Actuated(robot))
		self.addSequential(Do_Hp_Eject(robot))
		#self.addSequential(Do_Hp_Intake(robot))


