# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

from do_move_arm import Do_Move_Arm
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_max_arm_speed import Do_Max_Arm_Speed
from cargo_test import Cargo_Test
from do_cargo_intake import Do_Cargo_Intake
from do_cargo_eject import Do_Cargo_Eject
from do_hp_intake import Do_Hp_Intake
from do_hp_eject import Do_Hp_Eject
from do_hp_rotate_actuated import Do_Hp_Rotate_Actuated
from do_hp_rotate_unactuated import Do_Hp_Rotate_Unactuated
from do_ramp import Do_Ramp

from do_move_arm_nopid import Do_Move_Arm_NoPID

class OI():
	def __init__(self, robot):

		self.left_joy = robot.left_joy 
		self.right_joy = robot.right_joy 

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

		# Sets arm angle to 45 degrees
		ltop1.whileHeld(Do_Cargo_Eject(robot))		
		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))
		#XXX Change depending on test of PID or just P
		ltop3.whenPressed(Do_Move_Arm(robot, 15))
		#ltop3.whenPressed(Do_Move_Arm_NoPID(robot, 15.0))
		ltop4.whenPressed(Do_Encoder_Check(robot))
		lsomething.whenPressed(Do_Ramp(robot))
		# Determine the max speed of the arm for future operations
		# This is how the max speed of the arm was determined.
		#ltop2.whenPressed(Do_Max_Arm_Speed(robot))
		#rtop4.whenPressed(Do_Pid_Loop(robot))	

		rtop1.whenActive(Do_Hp_Intake(robot))
		rtop1.whenInactive(Do_Hp_Eject(robot))
		rtop2.whenActive(Do_Hp_Rotate_Actuated(robot))
		rtop2.whenInactive(Do_Hp_Rotate_Unactuated(robot))
		rtop3.whileHeld(Do_Cargo_Intake(robot))

