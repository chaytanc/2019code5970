# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# rotates/actuates Hatch Panel Intake inwards (closer to robot)
class Do_Hp_Rotate_Actuated(Command):
	def __init__(self, robot):
		super().__init__()
		
		# inherited subsystems
		self.robot_hatch_panel_rotate = robot.hatch_panel_rotate

		# uses solenoid 2
		'''
		Hatch Panel Intake can only be in two rotation states:
			1: actuated(intake) & Arm at robot front (0 degrees)
			2: unactuated(eject) & Arm at robot back (155 degrees)
			

		State 1: requires Hatch Panel Rotate
		'''
		self.requires(self.robot_hatch_panel_rotate)
		
	def initialize(self):
		# actuate Hatch Panel rotation pistons, retracting the intake
		self.robot_hatch_panel_rotate.hp_actuate()
		print("hatch panel rotation actuate!")

	def execute(self):
		return None

	def isFinished(self):
		return True

	def end(self):
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'hp_rotate_actuated' interrupted!")
		#self.cancel()
		self.end()
