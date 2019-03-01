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
from do_arm_test import Do_Arm_Test

# Non-button commands
from do_zeroed_clicks import Do_Zeroed_Clicks
from do_recal_clicks import Do_Recal_Clicks
from do_zero_encoder import Do_Zero_Encoder

# intake commands
from do_cargo_eject import Do_Cargo_Eject
#from do_cargo_intake import Do_Cargo_Intake
from do_hp_intake import Do_Hp_Intake
from do_hp_eject import Do_Hp_Eject

# shifter commands
from do_shifters_toggle import Do_Shifters_Toggle

# command groups
from command_hp_eject import Command_Hp_Eject
from command_hp_intake import Command_Hp_Intake
#from command_ramp import Command_Ramp

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

		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))
		# Input desired angle of arm
		ltop3.whenPressed(Do_Move_Arm(robot, 135.0))
		#XXX
		ltop4.whenPressed(Do_Encoder_Check(robot))
		ltop5.whileHeld(Do_Arm_Test(robot))

		# whenActive and whenInactive allows toggle between 2 commands
		
		# for testing in sim
		rtop5.toggleWhenPressed(Do_Axis_Button_5(robot))

		# turns on axis for xbox button 5. Must be activated in beginning. Test			# making axis triggers send interrupts

		# xbox left analog controls cargo eject/intake

		# when START on xbox pressed first time, turns on axis detection
		
		# when START on xbox pressed second time, turns off axis detection
		# and deploys ramp

		#Cargo Outtake (near back of robot) / Cargo Intake (front of robot)
		xboxSTART.toggleWhenPressed(Do_Axis_Button_5(robot))

		xboxBACK.toggleWhenPressed(Do_Shifters_Toggle(robot))
		# xbox XYBA controls arm positions
		# xbox X = Cargo Intake/Hatch Panel Outtake (front of robot)
		xboxX.whenPressed(Command_Hp_Eject(robot))
		# xbox Y = Defence Position (straight up)

		# xbox B = Hatch Panel Intake (back of robot)
		xboxB.whenPressed(Command_Hp_Intake(robot))	

		# xbox RB while held controls hp_intake(tennis balls)
		xboxRB.whileHeld(Do_Hp_Eject(robot))
		xboxRB.whenReleased(Do_Hp_Intake(robot))

		# Commands to be checked continually by Scheduler but not run
		# by direct button press:

		# Doesn't work because robotpy?
		#self.robot.arm_limit_switches.f_limit.requestInterrupts(
				#Do_Max_Encoder(robot))




