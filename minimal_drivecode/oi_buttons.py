# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from oi import OI
from wpilib.buttons import Trigger


from sys import path
path.append('../commands')

from do_encoder_check import Do_Encoder_Check

'''
Because commands need to call differential drive, they need access to joystick instances from oi.py

Importing oi does not work when the instance of the command is in oi.py itself.

The purpose of this file is to create instances of commands that would otherwise
be instantiate in oi.py, such as whenPressed() or toggleWhenActive()
'''
class OI_Buttons():
	def __init__(self, robot):

		self.oi = OI(self)

               
		self.oi.ltrig0.whenPressed(Do_Encoder_Check(robot))

		# toggle instead of when pressed
		#self.oi.ltrig0.toggleWhenActive(EncoderCheck(robot))
                    




		





