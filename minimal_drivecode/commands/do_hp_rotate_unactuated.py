# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
#import sys
#sys.path.append('../subsystems/pneumatics')
#from pneumatics import Pneuma
		
# Unacctuates pistons for hatch panel manipulator. Default and intake state.
class Do_Hp_Rotate_Unactuated(Command):
	def __init__(self, robot):
		
		super().__init__()
		
		self.robot_hatch_panel = robot.hatch_panel
		# overlaps with hp_eject and hp_intake requirement. May be problematic
		self.requires(self.robot_hatch_panel)
		
		self.robot_arm = robot.arm
		self.hp_rotate_solenoid = self.robot_hatch_panel.hp_rotate_solenoid
		
	def initialize(self):
		return None
	def execute(self):
		self.robot_hatch_panel.hp_unactuate(self.hp_rotate_solenoid)
		print("hatch panel rotation unactuate!")
	
	def isFinished(self):
		return True
	def end(self):
		return None
	def interrupted(self):
	    print("interrupted")
		#self.cancel()
		#self.end()

