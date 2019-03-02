# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# unactuates(low gear) Shifters
class Do_Shifters_Off(Command):
	def __init__(self, robot):
		super().__init__()

		# inherited subsystems
		self.robot_shifters = robot.shifters

		# can be called when robot is disabled
		self.setRunWhenDisabled(True)

		# uses solenoids 0 and 1
		'''
		Shifters can onlu be in two states:
			1: actuated(high gear)
			2: unactuated(low gear)

		State 2: requires Shifters
		'''
		self.requires(self.robot_shifters)


	def initialize(self):
		# unactuate solenoids for shifters
		self.robot_shifters.shifters_off()
		print("shifters off!")

	def execute(self):
		return None

	def isFinished(self):
		return None

	def end(self):
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'shifters_off' interrupted!")
		self.end()


