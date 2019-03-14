# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import InstantCommand
from wpilib.command import Command
from wpilib.command import WaitForChildren

class Do_Zero_Encoder(WaitForChildren):
# Should be run in parallel with Do_Move_Arm to check if 
#class Do_Zero_Encoder(Command):
	def __init__(self, robot):
		super().__init__()

		self.robot = robot
		#XXX Don't want it to interrupt the arm because then it will never get
		# off the limit switch after zeroing because it will constantly
		# interrupt and set to zero.
		#self.requires(self.robot.b_limit)
		self.encoder = self.robot.arm.l_arm_encoder
		self.limit_counter = self.robot.b_limit.counter

	def initialize(self):
		return None

	def execute(self):
		# Zeroes arm encoder when the limit switch was hit because the
		# counter identifies when it has been hit
		# Resetting encoder should stop moving the arm.
		self.counter.reset()
		print(self.counter.get())
		print("Checking if limit was hit")
		limit_status = self.robot.b_limit.check_counter()
		if limit_status:
			print("*********Hit switch: Resetting encoder!************")
			self.encoder.reset()
			# Should also interrupt Do_Move_Arm??

	def end(self):
		return None

	def isFinished(self):
		return None

	def interrupted(self):
		return None

	def isInterruptible(self):
		return False

