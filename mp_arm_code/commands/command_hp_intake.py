# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_hp_rotate_unactuated import Do_Hp_Rotate_Unactuated 
from do_profile_move import Do_Profile_Move

# positions Arm for Hatch_Panel_Intake
class Command_Hp_Intake(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# uses solenoids 3 & 4 and ctre motors 1 & 2
		'''
		Hatch Panel Intake can only be in two states:
			1: unactuated(intake) & Arm at robot front (155 degrees)
			2: unactuated(eject) & Arm at robot back (0 degrees)

		State 1
		'''
		# UNTESTED ANGLES
		self.addSequential(Do_Profile_Move(robot, 0.1))
		self.addSequential(Do_Hp_Rotate_Unactuated(robot))
		print("hp intake init!")



