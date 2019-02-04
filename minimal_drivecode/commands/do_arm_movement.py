# vim: set sw=4 noet ts=4 fileencoding=utf-8:

from wpilib.command import Command

class Do_Arm_Movement(Command):
	
	def __init__(self, robot, distance):
		super().__init__()
		self.robot = robot
		# Desired position or voltage or something
		self.requires(self.robot.drivetrain)
		self.requires(self.robot.arm)
		self.pid = wpilib.PIDController(
			0,
			0,
			0,
			lambda: self.robot.drivetrain.getDistance(),
			lambda d: self.robot.arm.setmotors(d,d))
			
		pid.setSetpoint(distance)
	
