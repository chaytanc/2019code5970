# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command
from do_move_arm import Do_Move_Arm
		
# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Intake(Command):
	def __init__(self, robot):
		super().__init__()
		
		self.requires(robot.arm)
		self.robot_cargo = robot.cargo
	
	def initialize(self):
		print("cargo intake!")
		Do_Move_Arm(robot, 0)
		self.robot_cargo.cargo_intake()

	def execute(self):
		pass
	
	def isFinished(self):
		return False

	def end(self):
		self.robot_cargo.cargo_reset()

	def interrupted(self):
		self.end()
