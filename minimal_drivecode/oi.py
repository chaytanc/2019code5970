# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib
from wpilib.buttons import JoystickButton
from wpilib.buttons import Trigger

from sys import path
path.append('../commands')

from do_encoder_check import Do_Encoder_Check
from do_pid_loop import Do_Pid_Loop
from do_motor_rate_test import Do_Motor_Rate_Test
from cargo_test import Cargo_Test

class OI():
	def __init__(self, robot):

		self.left_joy = robot.left_joy 
		self.right_joy = robot.right_joy 
		self.third_joy = robot.third_joy

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

		thirdtop1 = JoystickButton(self.third_joy, 1)
		thirdtop2 = JoystickButton(self.third_joy, 2)
		thirdtop3 = JoystickButton(self.third_joy, 3)


		ltop4.whenPressed(Do_Encoder_Check(robot))
		lsomething.whenPressed(Do_Motor_Rate_Test(robot))
		rtop4.whenPressed(Do_Pid_Loop(robot))	

		xbox = robot.xbox
		if xbox.getAButtonPressed():
			Do_Cargo_Eject_Pos(robot)
		

                    




		




