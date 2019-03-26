# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# rotates/actuates Hatch Panel Intake inwards (closer to robot)
class Do_Undo_Four_Bar(Command):
	def __init__(self, robot):
		super().__init__()
		
		self.requires(robot.hp_intake)
		# inherited subsystems
		self.hp_intake = robot.hp_intake

	def initialize(self):
		# actuate Hatch Panel rotation pistons, retracting the intake
		self.hp_intake.bars_unactuate()
		print("four bar unactuate!")

	def execute(self):
		return None

	def isFinished(self):
		return True

	def end(self):
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'undo_four_bar' interrupted!")
		self.end()
