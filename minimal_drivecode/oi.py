# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib import XboxController
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

# Button commands
from do_move_arm import Do_Move_Arm
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_cargo_intake import Do_Cargo_Intake
#from do_arm_test import Do_Arm_Test

# Non-button commands
from do_zeroed_clicks import Do_Zeroed_Clicks
from do_recal_clicks import Do_Recal_Clicks
from do_zero_encoder import Do_Zero_Encoder

# intake commands
from do_cargo_eject import Do_Cargo_Eject
from do_hp_intake import Do_Hp_Intake
from do_hp_eject import Do_Hp_Eject

# shifter commands
from do_shifters_toggle import Do_Shifters_Toggle

# command groups
from command_hp_eject import Command_Hp_Eject
from command_hp_intake import Command_Hp_Intake
from command_ramp import Command_Ramp
from command_defense import Command_Defense
from command_cargo_intake import Command_Cargo_Intake

# axis interpreters
from do_axis_button_5 import Do_Axis_Button_5



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
		ltop1.whileHeld(Do_Cargo_Eject(robot))

		# Button 2 shuts down arm
		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))

		# Input desired angle of arm
		ltop3.whenPressed(Do_Move_Arm(robot, 25.0))

		#XXX
		ltop4.whenPressed(Do_Encoder_Check(robot))

		ltop5.whileHeld(Do_Cargo_Intake(robot))


		'''
		Joystick 1 / Right Joystick Commands
		'''
		# Button 1 while held actuates hp_intake(tennis balls)
		# when released, retract and actuate hp_intake
		rtop1.whileHeld(Do_Hp_Eject(robot))
		rtop1.whenReleased(Do_Hp_Intake(robot))

		# Button 2 toggles shifters
		#rtop2.toggleWhenPressed(Do_Shifters_Toggle(robot))
		rtop2.whenPressed(Do_Cargo_Eject(robot))

		# All the way back, 0 deg
		rtop3.whenPressed(Command_Cargo_Intake(robot))

		# for testing in sim
		#rtop5.whenPressed(Do_Cargo_Intake(robot))
		rtop5.whileHeld(Do_Cargo_Intake(robot))


		'''
		Joystick 2 / Xbox Controller Commands
		'''	
		# when BACK pressed, turn on axis detection for cargo intake
		#Cargo Outtake (near back of robot) / Cargo Intake (front of robot)
		#xboxBACK.whenPressed(Do_Axis_Button_5(robot))
		xboxBACK.whenPressed(Command_Cargo_Intake(robot))

		# when START pressed, deploy ramp and reset pneumatics to unactuated
		xboxSTART.whenPressed(Command_Ramp(robot))

		# XYBA controls arm positions
		# X = Hatch Panel Outtake (front of robot, same angle as cargo intake)
		# All the way over, 150ish deg in reality
		xboxX.whenPressed(Command_Hp_Eject(robot))

		# Y = Defence Position (straight up)
		xboxY.whenPressed(Command_Defense(robot))

		# B = Hatch Panel Intake (back of robot)
		# 0 degrees ish
		xboxB.whenPressed(Command_Hp_Intake(robot))	




		# Commands to be checked continually by Scheduler but not run
		# by direct button press:

		# Doesn't work because robotpy?
		#self.robot.arm_limit_switches.f_limit.requestInterrupts(
				#Do_Max_Encoder(robot))




