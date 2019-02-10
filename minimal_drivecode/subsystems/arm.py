# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Subsystem

from arm_motors import Arm_Motors
from encoder import My_Arm_Encoder

# Control game pieces with arm
# Arm subsystem should contain arm commands to be called by scheduler.
# Should give wpilib pid the encoders for source of velocity
# Should give wpilib pid the constants
# Should contain arm command which contains pid which Sched. will call
# Should set new velocity of motors

class Arm(Subsystem):

	def __init__(self, robot):
		print("init")
		super().__init__()
		
		# Motors
		arm_motors_instance = Arm_Motors()
		l_arm_motor = arm_motors_instance.left_arm_motor
		r_arm_motor = arm_motors_instance.right_arm_motor

		# Encoders
		self.l_arm_encoder = My_Arm_Encoder(0,1)
		self.direction = self.l_arm_encoder.getDirection()

		#self.max_click_rate = #XXX clicks/second, find/estimate

		# Limit_switches arg=dio
		self.limit_switch = wpilib.DigitalInput(6)

	#def cargo_intake(self, motor):
		#self.set_arm_position(intake)
		#motor.set(1)

	# The rate is of clicks/sec NOT dist/second! See subsystems/encoder.py
	def get_click_rate(self):
		rate = self.l_arm_encoder.getRate()
		return rate

	# Converts encoder rate of clicks per second to -1 to 1 scale
	def convert_encoder_rate(self, current_clicks):
		rate_conversion = self.max_click_rate / current_clicks
		return rate_conversion

	# Where pid stores output distance to target pos. and where arm adjusts
	def set_cargo_eject_pos(self, rate, direction):
		motor_voltage = self.convert_encoder_rate(rate)
		# Moves arm by signified voltages; should move in opposite the last
		# direction sensed by arm encoder
		self.l_arm_motor(motor_voltage * (direction * -1))
		self.r_arm_motor(motor_voltage * (direction))
			
	# Actually ejects ball. Arm must be set correctly beforehand
	def cargo_eject(self, motor):
		# Cargo ball motor
		motor.set(-1)

	def zero_encoders(self, encoder):
		if self.limit_switch.get():
			encoder.reset()

	# Used to convert each different position(angle) the arm will stop at into 
	# a desired -1 to 1 voltage scale. This will then be converted into clicks
	# per second so that the inputs to the PID are all in clicks per second

	# Current and desired angles must be passed in as degrees
	def sin_relative_angle(self, current_angle, desired_angle):
		current_angle_radians = current_angle * math.pi/180
		desired_angle_radians = desired_angle * math.pi/180
		voltage = (math.sin((math.pi/desired_angle_radians)
				* current_angle_radians))
		return voltage

	def motor_test_max_speed(self):
		self.left_arm_motors.set(1)
		#self.right_arm_motors.set(-1)








# Preset actuated positions:
	# Straight up pos.
		# Get position using Encoder
		# Adjust motor velocity
		# Stop when target position is reached
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
	 
