# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.command import Command

# checks Xbox Controller axis inputs and run commands accordingly
class Do_Axis_Button_5(Command):
	'''
	Command functionally equivalent to "when controller axis is triggered, 
	do [command or command group]

	Responds to axis corresponding to xbox controller button 5
	'''
	def __init__(self, robot):
		super().__init__()
		
		# inherited subsystems
		self.robot = robot
		self.robot_cargo = robot.cargo
		self.robot_ramp = robot.ramp
		
		# keeps track of axis inputs over time
		self.previous_axis_input = 0
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		# initializes on [first press] of "Xbox controller 'BACK' button"
		#								OR
		# initializes on [first press] of "Joystick controller 1 '5' button"

	def execute(self):
		"""Called iteratively by Scheduler"""
		# continuously check current button axis input
		self.current_axis_input = self.robot.xbox.getRawAxis(1)
		# commandgroup for Cargo_Eject or Cargo_Intake based on button axis input
		self.robot_cargo.cargo_axis_commands(self.current_axis_input, 
				self.previous_axis_input)
		
		# record previous button axis input
		self.previous_axis_input = self.current_axis_input

	def isFinished(self):
		# continuously runs
		return None

	def end(self):
		return None
	
	def interrupted(self):
		print("Command 'axis_button_5' interrupted!")
		self.end()


	
