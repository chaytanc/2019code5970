# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
from sys import path
path.append('../commands')
from wpilib.command import Subsystem



class Hatch_Panel(Subsystem):
	#*********Robot-Side Initialization***************
	def __init__(self):
		super().__init__()
		# Command Dependencies:
		# Hatch Panel Rotate Actuated/Unactuated
		# Hatch Panel Intake/Eject

		#Initialize Pneumatics[hatch panel intake]
		self.hp_solenoid = wpilib.Solenoid(4)
		self.hp_rotate_solenoid = wpilib.Solenoid(5)

	def hp_actuate(self, solenoid):
		# actuate hatch panel intake
		solenoid.set(True)

	def hp_unactuate(self, solenoid):
		# unactuate hatch panel intake
		solenoid.set(False)


