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
		rate_conversion = #XXX self.max_click_rate / current_clicks
		return rate_conversion

	# Converts -1 to 1 scale voltage into a rate of clicks per second
	def convert_voltage_to_rate(self, voltage):
		click_rate = voltage * #XXX self.max_click_rate
		return click_rate

	# Used to convert each different position(angle) the arm will stop at into 
	# a desired -1 to 1 voltage scale. This will then be converted into clicks
	# per second so that the inputs to the PID are all in clicks per second

	# Gets current angle in degrees
	def get_current_angle(self):
		absolute_clicks = self.l_arm_encoder.get()	
		deg_per_click = self.l_arm_encoder.getDistancePerPulse()
		current_angle = absolute_clicks * deg_per_click	
		return current_angle

	# Current and desired angles must be passed in as degrees
	def sin_relative_angle(self, current_angle, sweep_angle):
		current_angle_radians = current_angle * math.pi/180
		sweep_angle_radians = sweep_angle * math.pi/180

		# Pi over desired angle is the period of 1/2 the sin wave,
		# such that the greatest angle which the are is intended to travel 
		# is the second x intercept of the sin wave, making velocity 
		# (y value) be zero.
		# Current angle in radians is the x input to the sin function and is
		# multiplied by the adjusted period of the sin wave to yield the
		# -1 to 1 scaled y value for velocity.
		voltage = (math.sin((math.pi/sweep_angle_radians)
				* current_angle_radians))
		return voltage

	# To define the setpoint, input the angle which you want the arm to stop at
	def get_setpoint(self, sweep_angle):
		angle = self.get_current_angle()
		voltage = self.sin_relative_angle(angle, sweep_angle)
		setpoint_rate = self.convert_voltage_to_rate(voltage)
		return setpoint_rate
		
	# Where pid stores output distance to target pos. and where arm adjusts
	def set_cargo_eject_pos(self, rate):
		motor_voltage = self.convert_encoder_rate(rate)
		# Moves arm by signified voltages; should move in opposite the last
		# direction sensed by arm encoder
		self.l_arm_motor(motor_voltage)
		self.r_arm_motor(motor_voltage)
			
	# Actually ejects ball. Arm must be set correctly beforehand
	def cargo_eject(self, motor):
		# Cargo ball motor
		motor.set(-1)

	def zero_encoders(self, encoder):
		if self.limit_switch.get():
			encoder.reset()


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
	 
