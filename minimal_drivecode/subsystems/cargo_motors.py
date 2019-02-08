# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Cargo_Motors():
 
	def __init__(self):
		#Initialize Left motors
		self.cargo_m = (wpilib.VictorSP(6))

				
