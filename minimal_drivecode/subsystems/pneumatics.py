# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')



class Pneuma():
	#*********Robot-Side Initialization***************
	def __init__(self):
		#Initialize Pneumatics[pistons]
		self.pistonL = wpilib.Solenoid(2)
		self.pistonR = wpilib.Solenoid(3)

		#Initialize Pneumatics[shifters]
		self.shiftL = wpilib.Solenoid(0)
		self.shiftR = wpilib.Solenoid(1)

		throttle = wpilib.Joystick(0)
		steering = wpilib.Joystick(1)

		# set actuate shifter button/?low gear?
		self.pop = JoystickButton(steering, 5)

		#Initialize Joystick Drive[steering] controls
			# throttle and steering were previously set here to joystick 0 and 1
			# these were moved to directly set the buttons because the joystick
			# in use is not an attribute of pneumatics systems; the buttons
			# used are?


		#Initialize Joystick Pneumatic[pistons] controls
		self.pn_button_L = JoystickButton(throttle, 1)
		self.pn_button_R = JoystickButton(steering, 1)
	'''
	Compress air for pistons?
	'''
	def pistons(self):
		### Pneumatic piston is off if the button is pressed???
		if self.pn_button_L.get():
			self.pistonL.set(False)
		else:
			self.pistonL.set(True)
		if self.pn_button_R.get():
			self.pistonR.set(False)
		else:
			self.pistonR.set(True)

	# Checks if button is pressed and actuates shifter accordingly
	def Pop(self):
		if self.pop.get():
			self.shiftL.set(True)
			self.shiftR.set(True)

		else:
			self.shiftL.set(False)
			self.shiftR.set(False)



