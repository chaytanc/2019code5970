# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger


from sys import path
path.append('../commands')

class OI():
	def __init__(self, robot):

		self.left_joy = wpilib.Joystick(0)	
		self.right_joy = wpilib.Joystick(1)	
		# First character indicates self.right or self.left, second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is self.left top 0 
		ltop1 = JoystickButton(self.left_joy, 1)
		ltop2 = JoystickButton(self.left_joy, 2)
		ltop3 = JoystickButton(self.left_joy, 3)
		self.ltrig0 = JoystickButton(self.left_joy, 4)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)

                    




		




