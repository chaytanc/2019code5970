# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import math
import wpilib
from wpilib.command import PIDSubsystem
from wpilib.command import Subsystem

from arm_motors import Arm_Motors
from encoder import My_Arm_Encoder

# Control game pieces with arm
# Arm subsystem should contain arm commands to be called by scheduler.
# Should give wpilib pid the encoders for source of velocity
# Should give wpilib pid the constants
# Should contain arm command which contains pid which Sched. will call
# Should set new velocity of motors

# PIDSubsystem?
class Arm(Subsystem):

	def __init__(self, robot):
		print("init")
		super().__init__()
		
		# Motors
		self.arm_motors = Arm_Motors()

		# Encoders
		self.l_arm_encoder = My_Arm_Encoder(0,1)

		#XXX accidental test reached 318, but with a 0.99 input
		# By empirical test
		self.max_click_rate = 340.0 

		# Limit_switches arg=dio
		self.limit_switch = wpilib.DigitalInput(6)

	
	#def cargo_intake(self, motor):
		#self.set_arm_position(intake)
		#motor.set(1)

#	# Actually ejects ball. Arm must be set correctly beforehand
#	def cargo_eject(self, motor):
#		# Cargo ball motor
#		motor.set(-1)

	# The rate is of clicks/sec NOT dist/second! See subsystems/encoder.py
	def get_click_rate(self):
		rate = self.l_arm_encoder.get_new_rate() * 1.0
		return

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
		print("current angle clicks: " + str(absolute_clicks))
		deg_per_click = self.l_arm_encoder.getDistancePerPulse()
		current_angle = absolute_clicks * deg_per_click	
		return current_angle

	# Final angle is the absolute angle between position of the arm at zero
	# clicks and when you want the arm to end up.
	# Sweep angle is angle between the current and final angles; may be equal
	# to final_angle if beginning at a 0 deg. or 180 deg. angle
	def get_sweep_angle(self, final_angle):
		sweep_angle = final_angle - self.get_current_angle()
		return sweep_angle

	# Current and final angles must be passed in as degrees
	def sin_angle(self, final_angle):
		current_angle_radians = self.get_current_angle() * math.pi/180
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
		setpoint_rate = self.voltage_to_click_rate(voltage)
		return setpoint_rate
		
	# A rate of 0 still stops motors, despite conversion
	# Where pid stores output distance to target pos. and where arm adjusts
	def set_motors(self, current_rate, use_min_speed=True):
		motor_voltage = self.click_rate_to_voltage(current_rate)

		# Moves arm motors by above voltages (actually values from -1 -> 1.0;
		# negative values should move in opposite the last direction sensed
		# by arm encoder
		print("Setting arm motor speed: " + str(motor_voltage))
		self.arm_motors.set_speed(motor_voltage, use_min_speed)
			
	def zero_encoders(self, encoder):
		if self.limit_switch.get():
			encoder.reset()

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
	 
