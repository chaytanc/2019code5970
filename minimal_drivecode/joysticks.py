# vim: set sw=4 noet ts=4 fileencoding=utf-8:

### Import all specific functions tied to buttons!?
# Assign all buttons to functions when button is pressed

lj = wpilib.Joystick(0)
rj = wpilib.Joystick(1)

	# If looping through this is too taxing just do this func
	# a million times, once per button assigned
def set_button(joystick, button_number):
	button = wpilib.buttons.JoystickButton(joystick, button_number)
	return button

def execute_button(button, func, *args=None):
	if button.get():
		func(*args)

# Xbox:
	# D-pad controls arm position for ejecting:
		# Cargo ship preset eject position
		# HP preset eject position
		# Low rocket eject position 
	# XYAB Buttons control arm position for intake:
		# Cargo and HP preset intake position
#		# Straight up position/starting position
	# Stick on xbox maybe continuously vary position of arm???
