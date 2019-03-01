# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
	
# Actuates pistons for hatch panel manipulator. Releasing hatch panel state.
class Do_Hp_Eject(Command):
	def __init__(self, robot):	
		super().__init__()
		
		self.robot_hatch_panel = robot.hatch_panel

		# uses solenoid 3
		
		# Hatch Panel can only be in two states:
		#	1: unactuated with Arm at back of robot. Actuates once.
		#	2: unactuated with Arm at front of robot

		# state 1: possesses Hatch Panel


		# hatch panel toggles between actuated and unactuated states
		# by [hold] or [release] of "Xbox controller 'RB' button"
		
		# [hold] toggles to actuated state
		self.requires(self.robot_hatch_panel)
		
	def initialize(self):
		# actuate Hatch Panel pistons, releasing hatch panel
		# immediatly unactuate Hatch Panel pistons
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
