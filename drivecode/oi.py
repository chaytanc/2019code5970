# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib import XboxController
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

# Button commands
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_beak_open import Do_Beak_Open
from do_four_bar import Do_Four_Bar
from do_undo_four_bar import Do_Undo_Four_Bar

# Non-button commands

# shifter commands
from do_shifters_toggle import Do_Shifters_Toggle

# command groups
#from command_ramp import Command_Ramp
#from command_defense import Command_Defense

class OI():
	def __init__(self, robot):

		self.robot = robot

		self.left_joy = robot.left_joy 
		self.right_joy = robot.right_joy 
		self.xbox = robot.xbox

		# First character indicates self.right or self.left, 
		# second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is self.left top 0 


		'''
		JoystickButton and Xbox button assignments
		'''
		ltop1 = JoystickButton(self.left_joy, 1)
		ltop2 = JoystickButton(self.left_joy, 2)
		ltop3 = JoystickButton(self.left_joy, 3)
		ltop4 = JoystickButton(self.left_joy, 4)
		ltop5 = JoystickButton(self.left_joy, 5)
		ltop6 = JoystickButton(self.left_joy, 6)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		rtop4 = JoystickButton(self.right_joy, 4)
		rtop5 = JoystickButton(self.right_joy, 5)
		rtop6 = JoystickButton(self.right_joy, 6)

		
		
		xboxX = JoystickButton(self.xbox, 3)
		xboxY = JoystickButton(self.xbox, 4)
		xboxB = JoystickButton(self.xbox, 2)
		xboxA = JoystickButton(self.xbox, 1)
		xboxLB = JoystickButton(self.xbox, 5)
		xboxRB = JoystickButton(self.xbox, 6)
		#xbox_left_XY = self.xbox.getY(9)
		#self.xbox_XY = JoystickButton(self.xbox, 9)
		self.xbox_left_XY = self.xbox.getX()
		xboxBACK = JoystickButton(self.xbox, 7)
		xboxSTART = JoystickButton(self.xbox, 8)


		# whenActive and whenInactive allows toggle between 2 commands
		'''
		Joystick 0 / Left Joystick Commands
		'''
		# Button 1 causes cargo motor to spin outwards for 0.5s
		#ltop1.whileHeld(Do_Cargo_Eject(robot))

		# Button 2 shuts down arm
		#ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))

		#XXX
		#ltop4.whenPressed(Do_Encoder_Check(robot))

		ltop5.whileHeld(Do_Beak_Open(robot))


		'''
		Joystick 1 / Right Joystick Commands
		'''
		# Button 2 toggles shifters
		rtop2.toggleWhenPressed(Do_Shifters_Toggle(robot))

		# All the way back, 0 deg

		# for testing in sim
		#rtop5.whenPressed(Do_Axis_Button_5(robot))


		'''
		Joystick 2 / Xbox Controller Commands
		'''	
		#xboxSTART.whenPressed(Command_Ramp(robot))

		# Y = Defence Position (straight up)
		#xboxY.whenPressed(Command_Defense(robot))

		# B = Hatch Panel Intake (front of robot)
		# B for BEAK
		xboxB.whileHeld(Do_Beak_Open(robot))	
		# Out of Frame
		xboxX.whenPressed(Do_Four_Bar(robot))
		# In frame
		xboxA.whenPressed(Do_Undo_Four_Bar(robot))


