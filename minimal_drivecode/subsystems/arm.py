# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import math
import wpilib
from wpilib.command import Subsystem
from wpilib import InterruptableSensorBase

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
		super().__init__()
		
		# Capslock because its a constant?
		# Added to current angle to account for max angle recalibration
		# Motors
		self.arm_motors = Arm_Motors()

		# Encoders
		self.l_arm_encoder = My_Arm_Encoder(0,1)

		# By empirical test
		self.max_click_rate = 318.0 


	# Called after back limit switch is hit
	#def set_zeroed_clicks(self):
		#self.zeroed_clicks = self.l_arm_encoder.get()

	# Called after back limit switch is hit
	#def set_rel_clicks(self):
		#self.rel_clicks = 146

	# The rate is of clicks/sec NOT dist/second! See subsystems/encoder.py
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

#XXX FOR FORWARD LIMIT SWITCH
#	# Gets current angle in degrees
#	def get_current_angle(self):
#		absolute_clicks = self.l_arm_encoder.get()
#		# Essentially zeroes encoder, but without changing the actual value,
#		# only changing the stored zeroed clicks value which is updated
#		# by limit switch and hereon used as base for encoder values
#		self.rel_clicks =  absolute_clicks - self.zeroed_clicks
#		#XXX prints for debugging
#		print("absolute encoder clicks: " + str(absolute_clicks))
#		deg_per_click = self.l_arm_encoder.getDistancePerPulse()
#		current_angle = rel_clicks * deg_per_click	
#		print("current angle, degrees: " + str(current_angle))

	# Final angle is the absolute angle between position of the arm at zero
	# clicks and when you want the arm to end up.
	# Sweep angle is angle between the current and final angles; may be equal
	# to final_angle if beginning at a 0 deg. or 180 deg. angle
	def get_sweep_angle(self, final_angle):
		sweep_angle = final_angle - self.get_current_angle()
		print("sweep angle" + str(sweep_angle))
		return sweep_angle

	#XXX Only run ONCE when initializing a command to move the arm so as to check
	# if the initial position the arm is in is greater than desired angle
	def get_initial_angle_offset(self, final_angle):
		if self.get_current_angle() > final_angle:
			# If the current angle is past what it is supposed to be at,
			# the current angle will be set to a bit greater than the current
			# angle such that the sin wave will return gentle negative voltages 
			# until the angle gets to being under what it is supposed to be,
			# at which point the regular sin wave values/pid take over.
			current_angle = final_angle * (5/3)

		# Sets angle to 1 degree so that no accidental negative encoder vals
		# occur
		else:
			current_angle = self.get_current_angle()
		return current_angle

	# Current and final angles must be passed in as degrees
	def sin_angle(self, final_angle):
		# Checks if angle is to far back
		current_angle_degrees = self.get_initial_angle_offset(
				 final_angle)

		current_angle_radians = current_angle_degrees * math.pi/180
		sweep_angle_radians = self.get_sweep_angle(final_angle) * math.pi/180

		# Pi over sweep angle is the period of 1/2 the sin wave,
		# such that the greatest angle which the arm is intended to travel 
		# is the second x intercept of the sin wave, making velocity 
		# (y value) be zero.
		# Current angle in radians is the x input to the sin function and is
		# multiplied by the adjusted period of the sin wave to yield the
		# -1 to 1 scaled y value for velocity.
		voltage = (math.sin((math.pi/sweep_angle_radians)
				* current_angle_radians))
		return voltage

	# To define the setpoint, input the angle which you want the arm to stop at
	# Relies on current_angle to be above 0 b/c of sin_angle
	def get_setpoint(self, final_angle):
		voltage = self.sin_angle(final_angle)
		print("voltage " + str(voltage))
		setpoint_rate = self.voltage_to_click_rate(voltage)
		return setpoint_rate

		
	# A rate of 0 still stops motors, despite conversion
	# Where pid stores output distance to target pos. and where arm adjusts
	def set_motors(self, current_rate, use_min_speed=True):
		motor_voltage = self.click_rate_to_voltage(current_rate)

		# Moves arm motors by above voltages (actually values from -1 -> 1.0;
		# negative values should move in opposite the last direction sensed
		# by arm encoder
		#XXX print for debugging
		print("Arm: Setting motor speed: " + str(motor_voltage))
		self.arm_motors.set_speed(motor_voltage, use_min_speed)
			


