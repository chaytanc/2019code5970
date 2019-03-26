# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_ramp import Do_Ramp
#from do_shifters_off import Do_Shifters_Off
from do_hp_rotate_unactuated import Do_Hp_Rotate_Unactuated
from do_hp_intake import Do_Hp_Intake

# activated at end of match
# positions Arm for Do_Ramp THEN resets pneumatics
class Command_Ramp(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# ramp uses solenoids 5 and ctre motors 1 & 2
		'''
		Ramp can only be in one state:
			1: actuated with Arm at [UNKNOWN POSITION]

		State 1
		'''

		# BEING WEIRD
		#self.addParallel(Do_Zero_Encoder(robot))
		self.addSequential(Do_Ramp(robot))
		
		# reset uses solenoids 0, 1, 2, 3
		# reset all non-ramp pneumatics to unactuated
		#self.addParallel(Do_Shifters_Off(robot))
		self.addParallel(Do_Hp_Rotate_Unactuated(robot))
		self.addParallel(Do_Hp_Intake(robot))

