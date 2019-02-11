# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
#from wpilib.buttons.joystickbutton import JoystickButton
import ctre

#*********Robot-Side Initialization***************
class Arm_Motors():
	
	def __init__(self):
		#Initialize Right motors
		#self.left_arm_motor = ctre.WPI_VictorSPX(1)	

		#XXX below motors are wired for testing!
		self.left_arm_motor = ctre.WPI_VictorSPX(3)
		self.right_arm_motor = ctre.WPI_VictorSPX(1)
			
	def set_speed(self, value):
		"""
		Sets the speed of the arm.  Max is 1.0 and moves the arm forward.
		Min is -1.0 and moves the arm backward.
		"""
		if value > 1 or value < -1:
			raise(RuntimeError, "arm given an invalid speed value: " + str(value))

		self.left_arm_motor.set(value)
		self.right_arm_motor.set(-value)



