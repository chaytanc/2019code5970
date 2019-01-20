# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Left_Motors():
 
	def __init__(self):
		#Initialize Left motors
		left_front = (wpilib.VictorSP(0))
		left_mid = (wpilib.VictorSP(1))
		left_rear = (wpilib.VictorSP(2))
		self.left_motor_group = wpilib.SpeedControllerGroup(
			left_front, left_mid, left_rear)

				
