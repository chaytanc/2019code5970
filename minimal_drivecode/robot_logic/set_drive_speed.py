def set_drive_motors(leftspeed, rightspeed):
	for motor in self.right.right_motors:
	            # One of these should be positive?
	            motor.set(leftspeed*-1)
	        for motor in self.left.left_motors:
	            motor.set(rightspeed*-1)

