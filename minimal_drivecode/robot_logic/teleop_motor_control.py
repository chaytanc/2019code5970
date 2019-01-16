import drive.py
def teleop_motor_control(left_throttle, right_throttle):
	#Initiate throttles

	#xbox definitions
	#left = self.xbox.getRawAxis(5)
	#right = self.xbox.getRawAxis(1)

	# Set tank inputs to be the y of the controller
	left = left_throttle.getY()
	right = right_throttle.getY()

	# drive is drive.py file
	drive_powers = drive.tankdrive(right*-1, left*-1)
	leftspeed = drive_powers[0]
	rightspeed = drive_powers[1]
	# set the motor speed to powers
	set_drive_motors(leftspeeds, rightspeeds)

