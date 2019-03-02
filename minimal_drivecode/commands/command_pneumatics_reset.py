# vim: set sw=4 noet ts=4 fileencoding=utf-8:

'''
UNUSED
'''
import wpilib
from wpilib.command import CommandGroup

# commands used in commandgroup
from do_hp_intake import Do_Hp_Intake
from do_shifters_off import Do_Shifters_Off
from do_hp_rotate_unactuated import Do_Hp_Rotate_Unactuated

# resets pneumatics
class Command_Pneumatics_Reset(CommandGroup):
	def __init__(self, robot):
		super().__init__()

		# can be called when robot is disabled
		self.setRunWhenDisabled(True)

		# resets all pneumatics except ramp to unactuated states
		# all pistons unactuate simultaneously

		# commandgroup called at when robot initially 
		# enters disabled (disabledInit in robot.py)
		self.addParallel(Do_Shifters_Off(robot))
		self.addParallel(Do_Hp_Rotate_Unactuated(robot))
		self.addParallel(Do_Hp_Intake(robot))


