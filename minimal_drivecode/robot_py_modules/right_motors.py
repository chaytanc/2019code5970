# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Right_Motors():
    
    #Initialize Right motors
    right_motors = []
	# I think you pass in the pdp channel to this??
    right_motors.append(wpilib.VictorSP(2))
    right_motors.append(wpilib.VictorSP(1))
    right_motors.append(wpilib.VictorSP(0))
