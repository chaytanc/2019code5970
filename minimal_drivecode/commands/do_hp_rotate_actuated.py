# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Actuates pistons for hatch panel manipulator. Releasing hatch panel state.
class Do_Hp_Rotate_Actuated(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		self.robot_hatch_panel_rotate = robot.hatch_panel_rotate
		self.robot = robot

		# uses solenoid 2
		
		# Hatch Panel Rotation can only be in two states:
		#	1: unactuated with Arm at back of robot
		#	2: actuated with Arm at front of robot

		# state 2: possesses Hatch Panel Rotate
		self.requires(self.robot_hatch_panel_rotate)
		
	def initialize(self):
		# move Arm to front of robot
		# Do_Move_Arm(self.robot, 100)
		# actuate Hatch Panel Rotation pistons, retracting the intake
		self.robot_hatch_panel_rotate.hp_actuate()
		print("hatch panel rotation actuate!")

	def execute(self):
		return None

	def isFinished(self):
		return True

	def end(self):
		return None

	def interrupted(self):
		print("interrupted")
		#self.cancel()
		self.end()
