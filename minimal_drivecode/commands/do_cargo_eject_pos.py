# vim: set sw=4 noet ts=4 fileencoding=utf-8:

from wpilib.command import Command
from wpilib.command import PIDCommand

# PIDCommand??
class Do_Cargo_Eject_Pos(Command):
	
	def __init__(self, robot):
		super().__init__()
		self.robot = robot
		# Desired position or voltage or something
		self.requires(self.robot.drivetrain)
		self.requires(self.robot.arm)
		# Target Distance/position
		#self.cargo_eject_target_dist = XXX some distance

		'''
		Each time PID is called in commands it can have a different input for
		setpoint which determines how close it is to being at the desired position.
		Each different position should have its own targetdistance
		'''
		encoder_kp = 1
		encoder_ki = 1
		encoder_kd = 1

		# Args: kp, ki, kd, source (function that will be called for vals),
		# output (somewhere to input the output percentage of what is input)
		self.pid = wpilib.PIDController(
			encoder_kp,
			encoder_ki,
			encoder_kd,
			# Gets arm encoder clicks per second
			self.robot.arm.l_arm_encoder.getRate(),
			### setmotors or something to rotate arm
			### cargo_eject both moves are and ejects cargo automatically
			### set_cargo_eject just moves the arm
			lambda d: self.robot.arm.set_cargo_eject(d))

		'''
		if self.robot.arm.l_arm_encoder < XXXlower_arm_range:
			self.cargo_eject_target_dist =+ slow_speed_target

		if self.robot.arm.l_arm_encoder > XXXhigher_arm_range:
			self.cargo_eject_target_dist =+ slow_speed_target

		if self.robot.arm.l_arm_encoder inRange \
		#  XXXmiddle_arm_range/peak of cos wave:
			self.cargo_eject_target =+ fast_target_speed

		'''
		pid.setSetpoint(self.cargo_eject_target_dist)

	def initialize(self):
		self.pid.reset()

	def execute(self):
		direction = robot.arm.l_arm_encoder.getDirection()
		# dist_from_target should be supplied by pid above
		robot.arm.set_cargo_eject(dist_from_target, direction)
		# Zeroes based on limit switches
		robot.arm.zero_encoders(robot.l_arm_encoder)
		

	def isFinished(self):
		# When another arm movement is called it can be interrupted
		# Does not do anything when finished/interrupted, just
		#if cancelled by other arm thing:
			#return True
		return None

	def end(self):
		# Do other command?
		# Slowly lower arm?	
		return None
	def interrupted(self):
		end()
		

	
