# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib

### Import all specific functions tied to buttons!?
# Assign all buttons to functions when button is pressed

class My_Joystick(wpilib.Joystick):	

	# If looping through this is too taxing just do this func
	# a million times, once per button assigned
	# Used to set variables to reference specific buttons
	def set_button(self, button_number):
		button = wpilib.buttons.JoystickButton(self, button_number)
		return button
	
	# Used to do functions when a button is pressed
	def do(self, button, func, *args):
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
