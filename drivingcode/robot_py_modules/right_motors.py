# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Right_Motors():
    
    #Initialize Right motors
    right_motors = []
    right_motors.append(wpilib.VictorSP(3))
    right_motors.append(wpilib.VictorSP(4))
    right_motors.append(wpilib.VictorSP(5))
