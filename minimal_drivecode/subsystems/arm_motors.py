# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
#from wpilib.buttons.joystickbutton import JoystickButton
import ctre

#*********Robot-Side Initialization***************
class Arm_Motors():
	OUTPUT_SCALE = 0.25
	MIN_SPEED = 0.20 / OUTPUT_SCALE
	
	def __init__(self):
		#Initialize Right motors
		#self.left_arm_motor = ctre.WPI_VictorSPX(1)	

		#XXX below motors are wired for testing!
		self.left_arm_motor = ctre.WPI_VictorSPX(3)
		self.right_arm_motor = ctre.WPI_VictorSPX(1)

	def set_speed(self, value, use_min_speed=False):
		"""
		Sets the speed of the arm.  Max is 1.0 and moves the arm forward.
		Min is -1.0 and moves the arm backward. OUTPUT_SCALE is multiplied
		times this value.  We need lower values because we only get about
		6 samples in a full range swing of the arm.
		"""
		if use_min_speed:
			if value >= 0.0:
				if value < self.MIN_SPEED:
					value = self.MIN_SPEED
			else:
				if value > -self.MIN_SPEED:
					value = -self.MIN_SPEED

		# Scale the speed to fall within our maximums
		value *= self.OUTPUT_SCALE

		print("Setting both arm motors to :" + str(value))
		if value > self.OUTPUT_SCALE or value < -self.OUTPUT_SCALE:
			raise RuntimeError(
				"arm given an invalid speed value: " + str(value))

		self.left_arm_motor.set(
			self.left_arm_motor.ControlMode.PercentOutput, value)
		self.right_arm_motor.set(
			self.right_arm_motor.ControlMode.PercentOutput, -value)
