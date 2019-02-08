# vim: set sw=4 noet ts=4 fileencoding=utf-8:
from wpilib.command import PIDSubsystem
from arm_motors import Arm_Motors

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
		l_arm_motor = arm_motors_instance.left_motor
		r_arm_motor = arm_motors_instance.right_motor

		# Encoders
		self.l_arm_encoder = wpilib.Encoder(0,1)
		self.direction = self.l_arm_encoder.getDirection()
		# encoder.setDistancePerPulse
		# (based on manufacturer rating and gear reduct.)
		#self.l_arm_encoder.setDistancePerPulse(XXX)

		self.max_click_rate = #XXX clicks/second, find/estimate

		# Limit_switches
		self.limit_switch = wpilib.DigitalInput(XXX # DIO Port) 

	#def cargo_intake(self, motor):
		#self.set_arm_position(intake)
		#motor.set(1)

	def get_click_rate(self):
		#XXX The rate is of distance/second NOT clicks/second!
		rate = self.l_arm_encoder.getRate()

	# Converts encoder rate of clicks per second to -1 to 1 scale
	def convert_encoder_rate(self, current_clicks):
		rate_conversion = self.max_click_rate / current_clicks
		return rate_conversion

	# Where pid stores output distance to target pos. and where arm adjusts
	def set_cargo_eject(self, rate, direction):
		motor_voltage = self.convert_encoder_rate(rate)
		# Moves arm by signified voltages; should move in opposite the last
		# direction sensed by arm encoder
		self.l_arm_motor(motor_voltage * (direction * -1))
		self.r_arm_motor(motor_voltage * (direction))
			
	# Actually ejects ball. Arm must be set correctly beforehand
	def cargo_eject(self, motor, dist_from_target=None, direction=None):
		# Doesn't set arm automatically if below is commented
		#self.set_cargo_eject(dist_from_target, direction)

		# Cargo ball motor
		motor.set(-1)

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
	 
