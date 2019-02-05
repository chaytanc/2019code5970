# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
import ctre

class Arm_Motors():
	def __init__():
		self.left_motor = ctre.WPI_VictorSPX(1)	
		self.right_motor = ctre.WPI_VictorSPX(2)	
		#self.arm_motor_group = wpilib.SpeedControllerGroup(
			#left_intake, right_intake) 
