# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

from do_move_arm import Do_Move_Arm
from do_arm_interrupt import Do_Arm_Interrupt
from do_encoder_check import Do_Encoder_Check
from do_max_arm_speed import Do_Max_Arm_Speed
from cargo_test import Cargo_Test

class OI():
	def __init__(self, robot):

		self.left_joy = robot.left_joy 
		self.right_joy = robot.right_joy 
		#self.third_joy = robot.third_joy

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

		#XXX Justin I don't think we use a third joystick
		#thirdtop1 = JoystickButton(self.third_joy, 1)
		#thirdtop2 = JoystickButton(self.third_joy, 2)
		#thirdtop3 = JoystickButton(self.third_joy, 3)


		# Sets arm angle to 45 degrees
		ltop2.whenPressed(Do_Arm_Interrupt(robot))
		ltop3.whenPressed(Do_Move_Arm(robot, 45))
		ltop4.whenPressed(Do_Encoder_Check(robot))

		# Determine the max speed of the arm for future operations
		# This is how the max speed of the arm was determined.
		#ltop2.whenPressed(Do_Max_Arm_Speed(robot))
		#rtop4.whenPressed(Do_Pid_Loop(robot))	


		xbox = robot.xbox
		if xbox.getAButtonPressed():
			Do_Cargo_Eject_Pos(robot)
		
