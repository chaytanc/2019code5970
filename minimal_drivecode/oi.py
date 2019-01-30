import wpilib
from wpilib.buttons import JoystickButton

class OI():
	# Why inherit the robot created in robot.py?
	def __init__(self, robot):
		self.left_joy = wpilib.Joystick(0)	
		self.right_joy = wpilib.Joystick(1)	
		
		# First character indicates self.right or self.left, second indicates position,
		# third indicates which button of the position specified
		# Ex: ltop0 is self.left top 0 
		ltop0 = JoystickButton(self.left_joy, 0)
		ltop1 = JoystickButton(self.left_joy, 1)
		ltop2 = JoystickButton(self.left_joy, 2)
		ltop3 = JoystickButton(self.left_joy, 3)
		ltrig0 = JoystickButton(self.left_joy, 4)

		rtop0 = JoystickButton(self.right_joy, 0)
		rtop1 = JoystickButton(self.right_joy, 1)
		rtop2 = JoystickButton(self.right_joy, 2)
		rtop3 = JoystickButton(self.right_joy, 3)
		rtrig0 = JoystickButton(self.right_joy, 4)

		




