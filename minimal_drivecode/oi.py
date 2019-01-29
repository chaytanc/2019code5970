import wpilib
from wpilib.buttons import JoystickButton

class OI():
	# Why inherit the robot created in robot.py?
	def __init__(self, robot):
		left_joy = wpilib.Joystick(0)	
		right_joy = wpilib.Joystick(1)	
		
		# First character indicates right or left, second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is left top 0 
		ltop0 = JoystickButton(left_joy, 0)
		ltop1 = JoystickButton(left_joy, 1)
		ltop2 = JoystickButton(left_joy, 2)
		ltop3 = JoystickButton(left_joy, 3)
		ltrig0 = JoystickButton(left_joy, 4)

		rtop0 = JoystickButton(right_joy, 0)
		rtop1 = JoystickButton(right_joy, 1)
		rtop2 = JoystickButton(right_joy, 2)
		rtop3 = JoystickButton(right_joy, 3)
		rtrig0 = JoystickButton(right_joy, 4)

		




