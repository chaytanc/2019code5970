# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')



class Hatch_Panel():
	#*********Robot-Side Initialization***************
	def __init__(self):

		#Initialize Pneumatics[hatch panel intake]
		self.hp_solenoid = wpilib.Solenoid(4)

	def hp_actuate(self, solenoid):
		# actuate hatch panel intake
		solenoid.set(True)

	def hp_unactuate(self, solenoid):
		# unactuate hatch panel intake
		solenoid.set(False)


