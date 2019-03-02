# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
#from wpilib.buttons.joystickbutton import JoystickButton
import ctre

#*********Robot-Side Initialization***************
class Arm_Motors():
	OUTPUT_SCALE = 0.25
	MIN_SPEED = 0.2 / OUTPUT_SCALE
	
	def __init__(self):
		#Initialize Right motors
		self.left_arm_motor = ctre.WPI_VictorSPX(3)
		self.right_arm_motor = ctre.WPI_VictorSPX(1)

	def set_speed(self, voltage, use_min_speed=False):
		"""
		Sets the speed of the arm.  Max is 1.0 and moves the arm forward.
		Min is -1.0 and moves the arm backward. OUTPUT_SCALE is multiplied
		times this voltage.  We need lower voltages because we only get about
		6 samples in a full range swing of the arm.
		"""

		if use_min_speed:
			if voltage >= 0.0:
				if voltage < self.MIN_SPEED:
					voltage = self.MIN_SPEED

					
			else:
				if voltage > -self.MIN_SPEED:
					voltage = -self.MIN_SPEED
					
		if use_min_speed == False:
			voltage = 0.22
				

		# Scale the speed to fall within our maximums
		voltage *= self.OUTPUT_SCALE

		print("Setting arm motors.py to :" + str(voltage))
		if voltage > self.OUTPUT_SCALE or voltage < -self.OUTPUT_SCALE:
			raise RuntimeError(
				"arm given an invalid speed voltage: " + str(voltage))

		self.left_arm_motor.set(
			self.left_arm_motor.ControlMode.PercentOutput, voltage)
		self.right_arm_motor.set(
			self.right_arm_motor.ControlMode.PercentOutput, -1 * voltage)
