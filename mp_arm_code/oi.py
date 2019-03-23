# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib import XboxController

from sys import path
path.append('../commands')

# Button commands
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_cargo_intake import Do_Cargo_Intake
from do_profile_move import Do_Profile_Move
from do_arm_go_back import Do_Arm_Go_Back
from do_cargo_eject import Do_Cargo_Eject
from do_hp_intake import Do_Hp_Intake
from do_hp_eject import Do_Hp_Eject
from do_hp_rotate_unactuated import Do_Hp_Rotate_Unactuated
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated


# Non-button commands
from do_zero_encoder import Do_Zero_Encoder

# shifter commands
from do_shifters_toggle import Do_Shifters_Toggle

# command groups
from command_hp_eject import Command_Hp_Eject
from command_hp_intake import Command_Hp_Intake
#XXX need to change for redesigned beak
#from command_ramp import Command_Ramp
from command_defense import Command_Defense
from command_cargo_intake import Command_Cargo_Intake
from command_cargo_eject_back import Command_Cargo_Eject_Back
from command_cargo_eject_forward import Command_Cargo_Eject_Forward

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
#		# Button 1 causes cargo motor to spin outwards for 0.5s
		ltop1.whenPressed(Do_Hp_Eject(robot))
#
#		# Button 2 shuts down arm
		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))
#
#		# Input desired angle of arm
#
		#ltop3.whenPressed(Do_Profile_Move(robot, 25.0))
		ltop3.whenPressed(Do_Cargo_Intake(robot))
#
#		#XXX
		ltop4.whenPressed(Do_Arm_Go_Back(robot))
		ltop5.whenPressed(Do_Profile_Move(robot, 150))
#
		#ltop5.whileHeld(XXX(robot))
#
#
#		'''
#		Joystick 1 / Right Joystick Commands
#		'''
#		# Button 1 while held actuates hp_intake(tennis balls)
#		# when released, retract and actuate hp_intake
		rtop1.whileHeld(Do_Hp_Intake(robot))

		#rtop1.whenReleased(XXX(robot))
#
#		# Button 2 toggles shifters
		rtop2.whileHeld(Do_Shifters_Toggle(robot))
		#rtop2.whileHeld(Do_Cargo_Eject(robot))
#
		#rtop3.whileHeld(XXX(robot))
#		# for testing in sim
#		#rtop5.whenPressed(XXX(robot))
#
#
#		'''
#		Joystick 2 / Xbox Controller Commands
#		'''	
#		# when BACK pressed, turn on axis detection for cargo intake
#		#Cargo Outtake (near back of robot) / Cargo Intake (front of robot)

		#xboxBACK.whenPressed(XXX(robot))
#
#		# while RB pressed, cargo motor C INTAKE
		#xboxRB.whileHeld(Command_Cargo_Intake(robot))
#		# when START pressed, deploy ramp and reset pneumatics to unactuated
#		xboxSTART.whenPressed(Command_Ramp(robot))
#
#		# XYBA controls arm positions
#		# X = Hatch Panel Outtake (front of robot, same angle as cargo intake)
#		# All the way over, 150ish deg in reality
		#xboxX.whenPressed(Command_Hp_Eject(robot))
#
#		# Y = Defence Position (straight up)
		#xboxY.whenPressed(Command_Defense(robot))
#
#		# B = Hatch Panel Intake (back of robot)
#		# 0 degrees ish
		#xboxB.whenPressed(Command_Hp_Intake(robot))	

		# 120ish maybe 110 
		#xboxA.whenPressed(Command_Cargo_Eject_Forward(robot))

		#xboxLB.whenPressed(Command_Cargo_Eject_Back(robot))
		xboxA.whenPressed(Do_Hp_Rotate_Actuated(robot))
		xboxY.whenPressed(Do_Hp_Rotate_Unactuated(robot))
		xboxB.whenPressed(Do_Hp_Intake(robot))
		xboxX.whenPressed(Do_Hp_Eject(robot))

