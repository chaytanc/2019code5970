# vim: set sw=4 noet ts=4 fileencoding=utf-8
### Only use if not using wpilib classes and making your own command subsystems
import wpilib
from wpilib.command import Command
import sys
sys.path.append('..')


class Do_Pid_Loop(Command):
	def __init__(self, robot):
	    super().__init__()
	    self.robot_dt = robot.drivetrain

	    self.left_joy = robot.left_joy
	    self.right_joy = robot.right_joy
			
	    #Temporary Requires
	    self.requires(self.robot_dt) 

	def initialize(self):
	    """Called just before this Command runs the first time"""
	    return None

	def execute(self):
	    """Called repeatedly when this Command is scheduled to run"""
		
	    # Get encoder values 
	    print(self.robot_dt.sin_relative_angle(45, 35))

	    # Required periodical call to Differential Drive
	    self.robot_dt.set_tank_speed(
		self.left_joy, self.right_joy, self.robot_dt.drive)
	
	def isFinished(self):
	    """Make this return true when this Command no longer needs to run execute()"""
	    return None

	def end(self):
	    """Called once after isFinished returns true"""
	    return None

	def interrupted(self):
	    """Called when another command which requires one or more of the same subsystems is scheduled to run"""
	    self.end()
