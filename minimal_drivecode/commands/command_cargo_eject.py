# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_move_arm import Do_Move_Arm

# positions Arm for Cargo_Eject
class Command_Cargo_Eject(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses motor 6 and ctre motors 1 & 2
		'''
		Cargo Intake can only be in two states:
			1: rotating inwards(intake) & Arm at robot front (0 degrees)
			2: rotating outwards(eject) & Arm at robot back (135 degrees)

		State 2
		'''

		# Estimate, pid is bad still
		#self.addSequential(Do_Move_Arm(robot, 35))
		print("commandgroup cargo eject initialized")


