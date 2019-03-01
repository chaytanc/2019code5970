# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
	
# actuates Hatch Panel Intake
class Do_Hp_Eject(Command):
	def __init__(self, robot):	
		super().__init__()
		
		#inherited subsystems
		self.robot_hatch_panel = robot.hatch_panel

		# uses solenoid 3
		'''
		Hatch Panel can only be in two states:
			1: unactuated(intake) & Arm at robot front (155 degrees)
			2: unactuated(eject) & Arm at robot back (0 degrees)

		State 2: requires Hatch Panel
		'''
		self.requires(self.robot_hatch_panel)

		# Hatch Panel Intake toggles between actuate and unactuate
		# by [hold] or [release] of "Joystick1 '1' button"
		
		# [hold] toggles to actuate

	def initialize(self):
		# actuate Hatch Panel Intake pistons, ejecting hatch panel
		self.robot_hatch_panel.hp_actuate()
		print("hatch panel actuate!")

	def execute(self):
		return None

	def isFinished(self):
		return True

	def end(self):
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'hp_eject' interrupted!")
		self.end()
