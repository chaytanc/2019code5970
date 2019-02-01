# vim: set sw=4 noet ts=4 fileencoding=utf-8:

# Get function for encoders, zero function for encoders
import wpilib
from wpilib.command import Subsystem
from sys import path
path.append('../commands')
from encoder_check import EncoderCheck


class Encoders(Subsystem):
	# Negative outputs of encoders are reverse direction counting
	#Don't initialize variables in init if you need it as an attribute
	def __init__(self, robot):
		super().__init__()
		self.robot = robot

	# Function to get encoder values:
		# 
		
	# Function to reset encoder values:
		# set encoder value to zero
		# encoder.reset()
	
	# Get encoder direction:	
	def get_direction(self):
		#direction = encoder.getDirection()
		#return direction  
		print(str("direction"))
