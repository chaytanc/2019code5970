# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# Unactuates pistons for hatch panel manipulator. Default and intake state.
class Do_Hp_Rotate_Unactuated(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		self.robot_hatch_panel_rotate = robot.hatch_panel_rotate
		self.robot = robot
		
		# uses solenoid 2

		# Hatch Panel Rotation can only be in two states:
		#	1: unactuated with Arm at back of robot
		#	2: actuated with Arm at front of robot
		
		# state 1: possesses Hatch Panel Rotate
		self.requires(self.robot_hatch_panel_rotate)
		
	def initialize(self):
		# move Arm to back of robot
		# Do_Move_Arm(self.robot, 0)
		# unactuate Hatch Panel Rotation pistons, loosening the intake
		self.robot_hatch_panel_rotate.hp_unactuate()
		print("hatch panel rotation unactuate!")

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

