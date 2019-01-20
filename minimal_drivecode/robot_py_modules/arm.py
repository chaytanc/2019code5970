# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Control game pieces with arm
class Arm():
	def __init__():
		print("init")
		
	def cargo_intake(self, button, motor):
		if button.get():
			set_arm_position(intake)
			motor.set(1)

	def cargo_eject(self, button, motor):
		if button.get():
			motor.set(-1)

# Initialize motors for controlling arm
# Initialize buttons here or import this and assign buttons there?
# Preset actuated positions:
	# Straight up pos.
		# Get position using Encoder
		# Adjust motor velocity
		# Stop when target position is reached
		# "Motion Magic" motion profiling??
	# Intake HP/Cargo pos.
	# Eject Cargo pos.
	# Eject HP pos.
	# Eject Rocket pos.

# Actuate things:
	#def cargo_intake():
		# set roller motor speeds 
	#def cargo_eject():
		# set roller motor speeds 
	#def hp_eject():
		# actuate pistons 
	 
