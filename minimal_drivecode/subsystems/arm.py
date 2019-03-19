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

		# By empirical test
		#self.max_click_rate = 318.0 

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
		self.max_accel = 0.636
		self.min_decel = 0.536

	#XXX Run in command initialization. End angle will be passed in in command
	def initialize(self):
		self.current_ticks = self.l_arm_encoder.get()
		#self.angle_displacement = self.get_angle_displacement(end_angle)

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
		current_pos = self.l_arm_encoder.get() - current_error
		return current_pos

	# Returns number of ticks necessary to get to the desired angle
#	#def angle_to_ticks(self, end_angle):
#		proportion = self.get_angle_displacement(end_angle)/self.angle_max
#		tick_displacement =(proportion * self.max_ticks)
#		return tick_displacement
#
#	def get_angle_displacement(self, end_angle):
#		# Find position accouting for error if at a limit switch
#		current_pos = self.position()
#		angle_displacement = end_angle - current_pos
#		return angle_displacement
#	
	# Number of ticks needed to travel from angle it is, sets vp accordingly
	def get_tick_displacement(self, end_angle):
		tick_displacement = int(self.angle_to_abs_clicks(end_angle) - \
			self.position())
		#self.vp = [318.0 for i in range(tick_displacement)]
		self.vp = [1.0 for i in range(tick_displacement)]
		for i in range(tick_displacement):
			self.x_axis_ticks.append(i)

	def forward_accel(self, feed_forward):
		self.vp[0] = feed_forward
		#XXX subtracted one from range len(self.vp)
		for i in range(1,len(self.vp)-1 ,1):
			self.vp[i] = min(self.vp[i],(self.vp[i-1]+self.max_accel))
		print("Arm: forward_accel: loop which sets vp: " + str(self.vp))
			
	def backwards_accel(self, feed_backward):
		self.vp[-1] = feed_backward
		for i in range(len(self.vp)-2, 0, -1):
			# Sets indexes of vp to the min value between the current index
			# value or the next vp plus the min value
			self.vp[i] = min(self.vp[i],(self.vp[i+1]+self.min_decel))
		print("Arm: backwards_accel: loop which sets vp: " + str(self.vp))
			
	def make_profile(self):
		self.forward_accel(0.35)
		self.backwards_accel(-0.35)

	# End angle is final angle not accounting for current angle
	def generate(self, end_angle):
		# Stores encoder value at the time of generating profile
		# (arm may move after using profile. Undesirable for generation values)
		self.get_tick_displacement(end_angle)
		self.encoder_start = self.current_ticks	
		# Creates velocity profile referenced in pick_motor_value
		print("Arm: generate!")
		self.make_profile()
		
	def pick_motor_value(self):
		# Gets the index relative to the profile of the ticks at the time of
		# generation. This is used to find the velocity based on the profile
		# and where the arm was when started
		#profile_ticks = current_tick_count - self.encoder_start
		#print("Arm: " + str(self.current_ticks))
		print("Arm: encoder: " + str(self.l_arm_encoder.get()))
		profile_ticks = self.l_arm_encoder.get() - self.encoder_start
		# vp means velocity profile
		desired_speed = self.vp[profile_ticks]
		print("Arm: pick_motor_value!")
		return desired_speed 

	#XXX
	def angle_to_abs_clicks(self, end_angle):
		# (403.2 * 12) / 360
		ticks = (end_angle * 13.44)
		return ticks


################################################################################
################################################################################
		
	# A rate of 0 still stops motors, despite conversion
	# Where pid stores output distance to target pos. and where arm adjusts
	# Input to this function must be a click rate
	def set_motors(self, input_rate):
		#motor_voltage = self.click_rate_to_voltage(input_rate)

		# Moves arm motors by above voltages (actually values from -1 -> 1.0;
		# negative values should move in opposite the last direction sensed
		# by arm encoder
		#XXX print for debugging
		print("Arm: Setting motor speed: " + str(input_rate))
		#self.arm_motors.set_speed(motor_voltage)
		self.arm_motors.set_speed(input_rate)
			


