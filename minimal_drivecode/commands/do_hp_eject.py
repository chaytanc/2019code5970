# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../subsystems/pneumatics')
#from pneumatics import Pneuma
		
# Actuates pistons for hatch panel manipulator. Releasing hatch panel state.
class Do_Hp_Eject(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		self.robot_hatch_panel = robot.hatch_panel
		self.requires(self.robot_hatch_panel)
		
		self.robot_arm = robot.arm
		self.hp_eject_solenoid = self.robot_hatch_panel.hp_solenoid
		
	def initialize(self):
		return None
	def execute(self):
		self.robot_hatch_panel.hp_actuate(self.hp_eject_solenoid)
		print("hatch panel actuate!")

	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
	    self.end()
