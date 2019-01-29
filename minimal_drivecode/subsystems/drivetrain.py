import wpilib
import wpilib.drive
from left_motors import Left_Motors()
from right_motors import Right_Motors()

class Drivetrain(Subsystem):
	def __init__():
		# Super from subsystem allows scheduler class to understand things like
		# interupt and execute etc...
		super().__init__()
	
		# Init motors here or import from robot.py
		left_motors_instance = Left_Motors()
		right_motors_instance = Right_Motors()
		left_motors = left_motors_instance.left_motor_group
		right_motors = right_motors_instance.right_motor_group

		# Set the drive train to use tank drive, self because used in commands
		self.drive = set_drivetrain_type(
			DifferentialDrive, left_motors, right_motors)

	# Sets driving mode to tank drive, should be periodically called
	def set_drivetrain_type(self, drivetrain_type, left_motors, right_motors):
		# DifferentialDrive for tank
		drive = wpilib.drive.drivetrain_type(left_motors, right_motors)
		return drive

	def set_tank_speed(self, left_joy, right_joy, drive):
		left_speed = left_joy.getY()
		right_speed = right_joy.getY()
		print("left_speed: " + str(left_speed))
		drive.tankDrive(left_speed, right_speed)

	def stop_robot(self, drive):
		drive.tankDrive(0,0)


		
		

