# vim: set sw=4 noet ts=4 fileencoding=utf-8:
from arm_motors import Arm_Motors

# Control game pieces with arm
class Arm(Subsystem):

	def __init__(self, robot):
		print("init")
		super().__init__()
		arm_motors_instance = Arm_Motors()
		arm_motors = arm_motors_instance.arm_motor_group
		self.eject_arm_position = XXX
		
	def cargo_intake(self, motor):
		self.set_arm_position(intake)
		motor.set(1)

	def cargo_eject(self, motor):
		self.set_arm_eject()
		motor.set(-1)

	#def set_arm_eject(self, motor):
		#velocity = pid_loop.get_velocity(target_velocity/voltage)
		#motor.set(velocity)
		
		
		

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
	 
