# vim: set sw=4 noet ts=4 fileencoding=utf-8:

import wpilib

#*********Robot-Side Initialization***************
class Right_Motors():
    
    #Initialize Right motors
    right_front = (wpilib.VictorSP(2))
    right_mid = (wpilib.VictorSP(1))
    right_rear = (wpilib.VictorSP(0))
	right_motor_group = wpilib.SpeedControllerGroup(
		right_front, right_mid, right_rear)


