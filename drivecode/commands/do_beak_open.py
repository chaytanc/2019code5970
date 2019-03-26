# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
		
# Closes Beak for Intake and Outtake
class Do_Beak_Open(Command):
	def __init__(self, robot):
		super().__init__()

		self.requires(robot.hp_intake)
		
		# inherited subsystems
		self.hp_intake = robot.hp_intake

		# can be called when robot is disabled
		#self.setRunWhenDisabled(True)

		# Hatch Panel Intake toggles between actuate and unactuate
		# by [hold] or [release] of "Joystick1 '1' button"
		# [release] toggles to unactuated state

	def initialize(self):
		# unactuate Hatch Panel Intake pistons, intaking hatch panel
		self.hp_intake.beak_actuate()
		print("beak open!")
	
	def execute(self):
		return None
	
	#def isFinished(self):
		#return True

	def end(self):
		# Closes beak when button stops being held
		self.hp_intake.beak_unactuate()
		print("beak close!")
		# pneumatics do not reset to unactuated position until robot shuts down
		return None

	def interrupted(self):
		print("Command 'beak open' interrupted!")
		self.end()

