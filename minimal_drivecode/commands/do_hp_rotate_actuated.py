# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../subsystems/pneumatics')
#from pneumatics import Pneuma
		
# Actuates pistons for hatch panel manipulator. Releasing hatch panel state.
class Do_Hp_Rotate_Actuated(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		# instance of drivetrain
		self.robot_dt = robot.drivetrain
		self.robot_hatch_panel = robot.hatch_panel
		# overlaps with hp_eject and hp_intake requirement. May be problematic
		self.requires(self.robot_hatch_panel)

		self.robot_arm = robot.arm
		self.hp_rotate_solenoid = self.robot_hatch_panel.hp_rotate_solenoid
		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
		


	def initialize(self):
		return True
	def execute(self):
		self.robot_hatch_panel.hp_actuate(self.hp_rotate_solenoid)
		print("hatch panel rotation actuate!")

		# Required periodical call to Differential Drive
		self.robot_dt.set_tank_speed(
			self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
	    self.end()
