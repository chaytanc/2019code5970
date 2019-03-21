# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
#from wpilib.buttons.joystickbutton import JoystickButton
import ctre

#*********Robot-Side Initialization***************
#XXX FOR PROFILING
class Arm_Motors():
	
	def __init__(self):
		#Initialize Right motors
		self.left_arm_motor = ctre.WPI_VictorSPX(3)
		self.right_arm_motor = ctre.WPI_VictorSPX(1)


	def set_speed(self, voltage):
		"""
		Sets the speed of the arm.  Max is 1.0 and moves the arm forward.
		Min is -1.0 and moves the arm backward. OUTPUT_SCALE is multiplied
		times this voltage.  We need lower voltages because we only get about
		6 samples in a full range swing of the arm.
		"""


		print("Arm motors: Setting to:" + str(voltage))

		self.left_arm_motor.set(
			self.left_arm_motor.ControlMode.PercentOutput, voltage)
		self.right_arm_motor.set(
			self.right_arm_motor.ControlMode.PercentOutput, -1 * voltage)
