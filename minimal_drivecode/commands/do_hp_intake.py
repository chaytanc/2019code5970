# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../subsystems/pneumatics')
#from pneumatics import Pneuma
		
# Unacctuates pistons for hatch panel manipulator. Default and intake state.
class Do_Hp_Intake(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		self.robot_hatch_panel = robot.hatch_panel
		
		self.robot_arm = robot.arm
		self.hp_intake_solenoid = self.robot_hatch_panel.hp_solenoid
		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy

		self.setTimeout(1)
		
	def initialize(self):
		return None
	def execute(self):
		self.robot_hatch_panel.hp_unactuate(self.hp_intake_solenoid)
		print("hatch panel unactuate!")

		# Required periodical call to Differential Drive
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
		return self.isTimedOut()
		print("Timed Out!")
	def end(self):
		return None
	def interrupted(self):
	    self.end()

