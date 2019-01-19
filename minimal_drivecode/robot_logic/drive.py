# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib

# Sets driving mode to tank drive, should be periodically called
def set_tank_drive(left_motors, right_motors):
	drive = wpilib.drive.DifferentialDrive(left_motors, right_motors)
	return drive

def set_tank_speed(left_joystick, right_joystick, drive):
	# Joysticks must be wpilib objects
	left_speed = left_joystick.getY()
	right_speed = right_joystick.getY()
	drive.tankdrive(left_speed, right_speed)

	
