# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
		
# Unactuates pistons for hatch panel manipulator. Default and intake state.
class Do_Hp_Intake(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		# instance of drivetrain
		self.robot_hatch_panel = robot.hatch_panel

		# uses solenoid 3
		
		# Hatch Panel can only be in two states:
		#	1: unactuated with Arm at back of robot. Primed for actuate
		#	2: unactuated with Arm at front of robot

		# state 2: possesses Hatch Panel


		# hatch panel toggles between actuated and unactuated states
		# by [hold] or [release] of "Xbox controller 'RB' button"

		# [release] toggles to unactuated state
		self.requires(self.robot_hatch_panel)

	def initialize(self):
		# unactuate Hatch Panel pistons, grabbing hatch panel
		self.robot_hatch_panel.hp_unactuate()
		print("hatch panel unactuate!")
	
	def execute(self):
		return None
	
	def isFinished(self):
		return True

	def end(self):
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'hp_intake' interrupted!")
		self.end()

