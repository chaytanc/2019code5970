# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

# arm commands
from do_move_arm import Do_Move_Arm
from do_die_you_gravy_sucking_pig import Do_Die_You_Gravy_Sucking_Pig
from do_encoder_check import Do_Encoder_Check
from do_max_arm_speed import Do_Max_Arm_Speed

from do_move_arm_nopid import Do_Move_Arm_NoPID

# intake commands
from do_cargo_eject import Do_Cargo_Eject
from do_cargo_intake import Do_Cargo_Intake
from do_hp_intake import Do_Hp_Intake

# shifter commands
from do_shifters_on import Do_Shifters_On
from do_shifters_off import Do_Shifters_Off

# command groups
from command_cargo_eject import Command_Cargo_Eject
from command_cargo_intake import Command_Cargo_Intake
from command_hp_eject import Command_Hp_Eject
from command_hp_intake import Command_Hp_Intake
from command_ramp import Command_Ramp

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
		ltop5 = JoystickButton(self.left_joy, 5)

		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		rtop4 = JoystickButton(self.right_joy, 4)

		# Sets arm angle to 45 degrees
		ltop1.whileHeld(Command_Cargo_Eject(robot))
		ltop2.whileHeld(Do_Die_You_Gravy_Sucking_Pig(robot))
		#XXX Change depending on test of PID or just P
		ltop3.whenPressed(Do_Move_Arm(robot, 15.0))
		#ltop3.whenPressed(Do_Move_Arm_NoPID(robot, 15.0))
		ltop4.whenPressed(Do_Encoder_Check(robot))
		ltop5.whenPressed(Command_Ramp(robot))
		# Determine the max speed of the arm for future operations
		# This is how the max speed of the arm was determined.
		#ltop2.whenPressed(Do_Max_Arm_Speed(robot))
		#rtop4.whenPressed(Do_Pid_Loop(robot))	

		# whenActive and whenInactive allows toggle between 2 commands
		rtop1.whenPressed(Command_Hp_Intake(robot))
		rtop2.whileHeld(Command_Hp_Eject(robot))
		rtop3.whileHeld(Command_Cargo_Intake(robot))
		rtop4.whenPressed(Do_Shifters_On(robot))
		rtop4.whenInactive(Do_Shifters_Off(robot))

