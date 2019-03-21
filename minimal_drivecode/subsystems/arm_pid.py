# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib
from wpilib.command import PIDSubsystem

from arm_motors import Arm_Motors
from encoder import My_Arm_Encoder

class Arm_Pid(PIDSubsystem):
	'''
	+- 135 degrees is max angle angle difference

		kP = (Target Angle - Current Angle)/(max angle difference)
		PID output is PROPORTIONAL to the % angle difference of the arm.
		The larger the angle difference, the closer motor output 
		speed is to +- 1. Converse is also true


	Left Joystick(0):
		Button 3: Target Angle = 25
		Button 4: Target Angle = 50


	PID Equation: 
		Motor Speed = Fudge Factor *(Target Angle - Current Angle) / 135
		Where -Motor Speed moves to back of robot (0) and + Motor Speed moves to		front of robot (135)

		ex. Current Angle = 35 & Target Angle = 50
			
			+15 Angles off-target ---> Motor Speed = 15/135 = 0.11
			Fudge Factor: Motor Speed = -0.11

			Current Angle = 65 & Target Angle = 50

			-15 Angles off-target ---> Motor Speed = -15/135 = -0.11
			Fudge Factor: Motor Speed = 0.11

	'''
	#kP = 1/135
	kP = 50/135
	kI = 0
	kD = 0

	def __init__(self, robot):
		super().__init__(self.kP, self.kI, self.kD, 0)

		# PID centers around target angle +- 1
		self.setAbsoluteTolerance(1)

		self.arm_motors = Arm_Motors()
		
		self.l_arm_encoder = My_Arm_Encoder(0,1)
		#self.counter = 50.0

		# 0 = false, 1 = true
		self.finished = 0

	def returnPIDInput(self):
		# counter test stuff
		#print(self.counter)
		#self.counter -=1
		#return self.counter

		return self.l_arm_encoder.getDistance()

	def usePIDOutput(self, output):
		# -1 fudge factor
		print("PID Output (pre-fudge): " + str(output))
		self.arm_motors.set_speed(-output)
	



