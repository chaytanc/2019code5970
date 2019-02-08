from wpilib.command import Command

# Should intake and outtake cargo (bouncy ball). This should be done by
# activating the motors for the rollers on the arm.
class Do_Cargo_Intake(Command):
	def __init___(self, robot):
		self.robot_arm = robot.arm
		cargo_motor = xxx
	
	def initialize():

	def execute():
		robot_arm.cargo_intake(cargo_motor)
	
	def isFinished():
	
	def end():
	
	def interrupted():
