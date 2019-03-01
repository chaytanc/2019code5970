# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
import wpilib.drive
from wpilib.command import Command
from command_pneumatics_reset import Command_Pneumatics_Reset


class Do_Axis_Button_5(Command):
	'''
	Command functionally equivalent to "when controller axis is triggered, 
	do [command or command group]

	Responds to axis corresponding to xbox controller button 5
	'''
	def __init__(self, robot):

		# recognize as a wpilib command
		super().__init__()
		

		# an instance of BeaverTronicsRobot from robot.py containing its
		self.robot = robot
		self.robot_cargo = robot.cargo
		self.robot_ramp = robot.ramp
		
		# keeps track of axis inputs over time
		self.previous_axis_input = 0
	
	def initialize(self):
		"""Called just before this Command runs the first time"""
		# initializes on [first press] of "Xbox controller 'START' button"
		#								OR
		# initializes on [first press] of "Joystick controller 1 '5' button"

	
	def execute(self):
		"""Called iteratively by Scheduler"""
		# continuously check current button axis input
		self.current_axis_input = self.robot.xbox.getRawAxis(1)
		# calls command based on button axis input
		self.robot_cargo.cargo_axis_commands(self.current_axis_input, 
				self.previous_axis_input)
		
		# record previous button axis input
		self.previous_axis_input = self.current_axis_input

	def isFinished(self):
		# continuously runs
		return None

	def end(self):
		# ends on [second press] of "Xbox controller 'START' button"
		#								OR
		# ends on [second press] of "Joystick controller 1 '5' button" 
		
		# stops checking axis input THEN actuates ramp THEN resets pneumatics
		self.robot_ramp.ramp_actuate()
		print("ramp actuated")
		Command_Pneumatics_Reset(self.robot)
		print("pneumatics reset")
	
	def interrupted(self):
		print("Command 'axis_button_5' interrupted!")
		self.end()


	
