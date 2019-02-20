# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

# Button commands
from do_move_arm import Do_Move_Arm
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_cargo_intake import Do_Cargo_Intake
from do_cargo_eject import Do_Cargo_Eject
from do_hp_intake import Do_Hp_Intake
from do_hp_eject import Do_Hp_Eject

# Non-button commands
from do_zeroed_clicks import Do_Zeroed_Clicks
from do_recal_clicks import Do_Recal_Clicks
from do_zero_encoder import Do_Zero_Encoder


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
		lsomething = JoystickButton(self.left_joy, 5)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		rtop4 = JoystickButton(self.right_joy, 4)

		xboxA = JoystickButton(self.xbox, 1)
		xboxB = JoystickButton(self.xbox, 2)
		xboxX = JoystickButton(self.xbox, 3)
		xboxY = JoystickButton(self.xbox, 4)

		ltop1.whileHeld(Do_Cargo_Eject(robot))		
		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))
		# Input desired angle of arm
		ltop3.whenPressed(Do_Move_Arm(robot, 15.0))
		ltop4.whenPressed(Do_Encoder_Check(robot))

		rtop1.whileHeld(Do_Hp_Intake(robot))
		rtop1.whenReleased(Do_Hp_Eject(robot))
		rtop1.cancelWhenPressed(Do_Hp_Eject(robot))
		rtop3.whileHeld(Do_Cargo_Intake(robot))

		# Commands to be checked continually by Scheduler but not run
		# by direct button press:

		#self.robot.arm_limit_switches.f_limit.requestInterrupts(
				#Do_Max_Encoder(robot))

		#self.robot.f_limit.requestInterrupts(Do_Recal_Clicks(robot))
		#self.robot.b_limit.requestInterrupts(Do_Zeroed_Clicks(robot))
		#self.robot.b_limit.requestInterrupts(Do_Zero_Encoder(robot))



