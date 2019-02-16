# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
from do_move_arm import Do_Move_Arm

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Eject(Command):
	def __init__(self, robot):
		
		super().__init__()

		self.robot_cargo = robot.cargo
		self.requires(robot.arm)
		self.robot = robot
	
	def initialize(self):
		Do_Move_Arm(self.robot, 100)
		self.robot_cargo.cargo_eject(self.cargo_motor)
		print("cargo eject!")

	def execute(self):
		return None

	def isFinished(self):
		return None

	def end(self):
		self.robot_cargo.cargo_reset(self.cargo_motor)

	def interrupted(self):
		self.end()

