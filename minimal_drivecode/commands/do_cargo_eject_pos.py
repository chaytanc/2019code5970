# vim: set sw=4 noet ts=4 fileencoding=utf-8:

from wpilib.command import Command
from wpilib.command import PIDCommand

# Inherits from command group
class Do_Cargo_Eject_Pos(Command):
	
	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		# Desired position or voltage or something
		self.requires(self.robot.drivetrain)
		self.requires(self.robot.arm)


	def initialize(self):
		self.pid.reset()

	def execute(self):
		# Move Arm Command
		# Eject Cargo Command
		robot.arm.zero_encoders(robot.l_arm_encoder)
		
	def isFinished(self):
		# When another arm movement is called it can be interrupted
		# Does not do anything when finished/interrupted, just
		# if cancelled by other arm thing:
			#return True
		return None

	def end(self):
		# Do other command?
		# Slowly lower arm?	
		return None

	def interrupted(self):
		self.end()
		

	
