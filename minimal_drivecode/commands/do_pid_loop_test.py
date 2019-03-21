# vim: set sw=4 noet ts=4 fileencoding=utf-8:

'''

import wpilib
from wpilib.command import Command
import sys
sys.path.append('..')


class Do_Pid_Loop_Test(Command):
	#init distance
	def __init__(self, robot, target_angle):
		super().__init__()
		self.robot_arm = robot.arm

		self.target_angle = target_angle

		self.left_joy = robot.left_joy
		self.right_joy = robot.right_joy
			
		#Temporary Requires
		self.requires(self.robot_arm)

		self.kP = 1
		self.kI = 0
		self.kD = 0
		self.kF = 1

		
	
		
		# 6 pulses per rev for encoder


	def initialize(self):
		"""Called just before this Command runs the first time"""
		#encoder resets every __init__ not every initialize. Every teleop should track angular distance entire teleop period
		# test absolute tolerance
		# test dynamic motor speed in response to PID feedback
		self.pid = wpilib.PIDController(self.kP, self.kI, self.kD, self.kF,
											lambda: self.robot_arm.arm_encoder_get(),
											lambda r: self.robot_arm.adjust_arm(r))
		self.pid.reset()
		self.pid.setContinuous(False)
		self.pid.setAbsoluteTolerance(0)
	
		self.pid.enable()

	def execute(self):
		print(str(self.pid.getError()) +  " output " + str(self.pid.get()) + " feed forward" + str(self.pid.pidWrite(10.0)))
		self.pid.setSetpoint(self.target_angle)
	
	def isFinished(self):
		#if self.pid.onTarget():
		return False

	def end(self):
		self.pid.disable()
		self.pid.close()
		print("Do_Move_Arm: Ending Command Do_Move_Arm")

	def interrupted(self):
		self.end()
'''

from wpilib.command import Command


class Do_Pid_Loop_Test(Command):

	def __init__(self, robot, setpoint):
		super().__init__()
		self.robot = robot

		self.setpoint = setpoint
		self.requires(self.robot.arm_pid)
		self.robot.arm_pid.l_arm_encoder.reset()
		

	def initialize(self):
		self.robot.arm_pid.enable()
		self.robot.arm_pid.setSetpoint(self.setpoint)
		

	def execute(self):
		#print(str(self.robot.arm_pid.usePIDOutput(self.setpoint)))
		print("PID Input: " + str(self.robot.arm_pid.getPosition()))
		#print(str(self.robot.arm_pid.returnPIDInput()))	
		#print(self.robot.arm_pid.getPIDController())
		return None

	def isFinished(self):
		return self.robot.arm_pid.onTarget()

	def end(self):
		self.robot.arm_pid.disable()
		self.robot.arm_pid.close()
		print ("disabled pid")
		self.robot.arm_pid.finished = 1


	def interrupted(self):
		self.end()
		self.robot.arm_pid.finished = 0


