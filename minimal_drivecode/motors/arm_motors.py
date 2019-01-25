import wpilib
import ctre

class Arm_Motors():
	def __init__():
		left_intake = ctre.WPI_VictorSPX(devicenumber)	
		right_intake = ctre.WPI_VictorSPX(devicenumber)	
		self.intake_motor_group = wpilib.SpeedControllerGroup(
			left_intake, right_intake) 
	
