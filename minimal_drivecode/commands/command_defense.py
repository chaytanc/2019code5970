# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated 
from do_move_arm import Do_Move_Arm
from do_zero_encoder import Do_Zero_Encoder

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

		# BEING WEIRD
		self.addParallel(Do_Zero_Encoder(robot))
		self.addSequential(Do_Move_Arm(robot, 90))
		print("commandgroup defense initialized")



