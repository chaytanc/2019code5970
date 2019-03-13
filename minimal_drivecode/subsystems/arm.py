# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import math
import wpilib
from wpilib.command import Subsystem

from arm_motors import Arm_Motors
from encoder import My_Arm_Encoder
from back_switch import Back_Switch

# Control game pieces with arm
# Arm subsystem should contain arm commands to be called by scheduler.
# Should give wpilib pid the encoders for source of velocity
# Should contain arm command which contains pid which Sched. will call
# Should set new velocity of motors

class Arm(Subsystem):

	def __init__(self, robot):
		super().__init__()
		
		# Capslock because its a constant?
		# Added to current angle to account for max angle recalibration
		# Motors
		self.arm_motors = Arm_Motors()
		limit = Back_Switch()
		self.back_switch = limit.back_switch

		# Encoders
		self.l_arm_encoder = My_Arm_Encoder(0,1)
		#self.l_arm_encoder = wpilib.Encoder(0, 1)

		# By empirical test
		self.max_click_rate = 318.0 

		# For getting encoder and accounting for limits and error
		# Arm starts in downward position
		self.arm_min_or_max = 0
		#XXX experimentally tested
		self.max_ticks = 434
		self.last_encoder = 0

		# For creating the profile (arm profile)
		self.x_axis_ticks = []
		# XXX angle max may be wrong
		self.angle_max = 150
		# Slope of profile
		self.max_accel = 0.536
		self.min_decel = 0.536

	#XXX Run in command initialization. End angle will be passed in in command
	def initialize(self, end_angle):
		self.current_ticks = self.l_arm_encoder.get()
		self.angle_displacement = self.get_angle_displacement(end_angle)

	def forward_limit(self):
		self.arm_min_or_max = self.max_ticks
		self.last_encoder = self.l_arm_encoder.get()
		
	def rearward_limit(self):
		self.arm_min_or_max = 0
		# Uses l arm encoder.get instead of current ticks because
		# it uses the actual value to calculate error
		self.last_encoder = self.l_arm_encoder.get()
		
	# Returns position in ticks accounting for error
	def position(self):
		current_error = self.arm_min_or_max - self.last_encoder
		current_pos = self.current_ticks - current_error
		return current_pos

	# Returns number of ticks necessary to get to the desired angle
	def angle_to_ticks(self, end_angle):
		proportion = self.get_angle_displacement(end_angle)/self.angle_max
		tick_displacement = int(proportion * self.max_ticks)
		return tick_displacement

	def get_angle_displacement(self, end_angle):
		# Find position accouting for error if at a limit switch
		current_pos = self.position()
		angle_displacement = end_angle - current_pos
		return angle_displacement
	
	def get_tick_displacement(self):
		tick_displacement = self.angle_to_ticks(self.max_ticks)
		self.vp = [318.0 for i in range(tick_displacement)]
		for i in range(tick_displacement):
			self.x_axis_ticks.append(i)

	def forward_accel(self, feed_forward):
		self.vp[0] = feed_forward
		for i in range(1,len(self.vp),1):
			self.vp[i] = min(self.vp[i],(self.vp[i-1]+self.max_accel))
			
	def backwards_accel(self, feed_backward):
		self.vp[-1] = feed_backward
		for i in range(len(self.vp)-2, 0, -1):
			self.vp[i] = min(self.vp[i],(self.vp[i+1]+self.min_decel))
			
	def make_profile(self):
		self.forward_accel(100)
		self.backwards_accel(50)

	# End angle is final angle not accounting for current angle
	def generate(self, end_angle):
		# Stores encoder value at the time of generating profile
		# (arm may move after using profile. Undesirable for generation values)
		#angle_displacement = self.get_angle_displacement(end_angle)
		self.get_tick_displacement()
		self.encoder_start = self.current_ticks	
		#XXX max accel min decel 700, 700)
		# Creates velocity profile referenced in pick_motor_value
		print("Arm: generate!")
		self.make_profile()
		
	def pick_motor_value(self):
		# Gets the index relative to the profile of the ticks at the time of
		# generation. This is used to find the velocity based on the profile
		# and where the arm was when started
		#profile_ticks = current_tick_count - self.encoder_start
		profile_ticks = self.current_ticks - self.encoder_start
		# vp means velocity profile
		desired_speed = self.vp[profile_ticks]
		print("Arm: pick_motor_value!")
		return desired_speed 


################################################################################
	# The rate is of clicks/sec NOT dist/second! See subsystems/encoder.py
	# Needed for pid input
	def get_click_rate(self):
		# Time 1.0 for float
		rate = self.l_arm_encoder.get_new_rate() * 1.0
		return rate

	# Converts encoder rate of clicks per second to -1 to 1 scale
	def click_rate_to_voltage(self, current_click_rate):
		rate_conversion = current_click_rate / self.max_click_rate
		return rate_conversion

	# Converts -1 to 1 scale voltage into a rate of clicks per second
	def voltage_to_click_rate(self, voltage):
		click_rate = voltage * self.max_click_rate
		return click_rate

	# Used to convert each different position(angle) the arm will stop at into 
	# a final -1 to 1 voltage scale. This will then be converted into clicks
	# per second so that the inputs to the PID are all in clicks per second

	# Gets current angle in degrees
	def get_current_angle(self):
		absolute_clicks = self.l_arm_encoder.get()	
		#XXX prints for debugging
		#print("absolute encoder clicks: " + str(absolute_clicks))
		deg_per_click = self.l_arm_encoder.getDistancePerPulse()
		current_angle = absolute_clicks * deg_per_click	
		print("current angle, degrees: " + str(current_angle))
		# Adds one degree to account for encoder skips which
		# cause negative values for encoder angle and uses
		# min drive speed (-0.2) for setting the motors
		return current_angle + 2.5

################################################################################
		
	# A rate of 0 still stops motors, despite conversion
	# Where pid stores output distance to target pos. and where arm adjusts
	# Input to this function must be a click rate
	def set_motors(self, current_rate, use_min_speed=True):
		motor_voltage = self.click_rate_to_voltage(current_rate)

		# Moves arm motors by above voltages (actually values from -1 -> 1.0;
		# negative values should move in opposite the last direction sensed
		# by arm encoder
		#XXX print for debugging
		print("Arm: Setting motor speed: " + str(motor_voltage))
		self.arm_motors.set_speed(motor_voltage)
			


