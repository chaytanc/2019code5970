# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
# vim: set sw=4 noet ts=4 fileencoding=utf-8:
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated 
from do_profile_move import Do_Profile_Move

# positions Arm for playing defense
class Command_Defense(CommandGroup):
	def __init__(self, robot):
		super().__init__()
		
		# uses ctre motors 1 & 2
		'''
		Defense can only be in one state:
			1: Arm at robot midpoint(90 degrees)

		State 1
		'''

		# Estimated angle accounting for weird pid
		self.addSequential(Do_Profile_Move(robot, 90))
		self.addSequential(Do_Hp_Rotate_Actuated(robot))
		print("defense!")



