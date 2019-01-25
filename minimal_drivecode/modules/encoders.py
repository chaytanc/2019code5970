# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Get function for encoders, zero function for encoders
import wpilib


class Encoders():
	# Negative outputs of encoders are reverse direction counting
	#Don't initialize variables in init if you need it as an attribute
	#def __init__(self):
	'''
		#Initialize Encoders
		right_encoder = wpilib.Encoder(2,3)
		left_encoder = wpilib.Encoder(0,1)
		arm_encoder = wpilib.Encoder(4,5)
	'''
	#Rcoder = wpilib.Encoder(2,3)
	#Lcoder = wpilib.Encoder(0,1)
	#Gcoder = wpilib.Encoder(4,5)
	
	# Get encoder values:
		# 
		
	# Zero encoder values:
		# set encoder value to zero
		# encoder.reset()
	
	# Get encoder direction:	
	def get_direction(self, encoder):
		direction = encoder.getDirection()
		return direction  
		
