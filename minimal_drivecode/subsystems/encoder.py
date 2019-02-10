# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib

class My_Arm_Encoder(wpilib.Encoder):

	# Class constants; change if encoder or drive ratios change
	DEGREE_PER_CLICK = 30.0
	DRIVE_RATIO = 1.0/403.2
	FINAL_DEGREE_PER_CLICK = DEGREE_PER_CLICK * DRIVE_RATIO

	def __init__(self, DIO_1, DIO_2):
		super().__init__(DIO_1, DIO_2)
		# Amount some gear in motor configuration turns per encoder click
		self.setDistancePerPulse(self.FINAL_DEGREE_PER_CLICK)
	
	def getRate(self):
		distance_per_seconds = super().getRate()
		clicks_per_sec = (
			distance_per_seconds / self.getDistancePerPulse()
			)
		return clicks_per_sec
