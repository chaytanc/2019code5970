import wpilib.command

class My_Arm_Encoder(wpilib.Encoder):
	def __init__(self, DIO_1, DIO_2):
		super().___init__()
		# Amount some gear in motor configuration turns per encoder click
		self.setDistancePerPulse(1/12)
	`
	def getRate():
		distance_per_seconds = self.encoder.getRate()
		super().getRate()
		clicks_per_sec = (
			distance_per_seconds / self.encoder.getDistancePerPulse
			)
