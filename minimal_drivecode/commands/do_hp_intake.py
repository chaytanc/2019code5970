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
		self.robot_hatch_panel = robot.hatch_panel
		self.requires(self.robot_hatch_panel)
		
		self.robot_arm = robot.arm
		self.hp_intake_solenoid = self.robot_hatch_panel.hp_solenoid

	def initialize(self):
		return None
	def execute(self):
		self.robot_hatch_panel.hp_unactuate(self.hp_intake_solenoid)
		print("hatch panel unactuate!")
	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
	    self.end()

