# vim: set sw=4 sts=4 fileencoding=utf-8:

### Import all specific functions tied to buttons!?
# Assign all buttons to functions when button is pressed

# Joystick Left:
	# Cargo eject trigger
		#cargo_eject = JoystickButton(joystick left or right, button_number)
		# wpilib.buttons.cargo_eject.whenPressed(arm.cargo_eject())
	# Ramp deploy button
	# Ramp up button

# Joystick Right:
	# HP eject trigger
		#hp_eject = JoystickButton(joystick, button)
		#wpilib.buttons.hp_eject.whenPressed(arm.hp_eject())
	# Vision auto line up button and eject HP
	# Switch to high gear button
	#

# Xbox:
	# D-pad controls arm position for ejecting:
		# Cargo ship preset eject position
		# HP preset eject position
		# Low rocket eject position 
	# XYAB Buttons control arm position for intake:
		# Cargo and HP preset intake position
		# Straight up position/starting position
	# Stick on xbox maybe continuously vary position of arm???
