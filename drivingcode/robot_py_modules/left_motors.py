# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Left_Motors():
 
    #Initialize Left motors
    left_motors = []
    left_motors.append(wpilib.VictorSP(13))
    left_motors.append(wpilib.VictorSP(14))
    left_motors.append(wpilib.VictorSP(15))
                
