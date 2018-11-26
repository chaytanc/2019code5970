import wpilib
from wpilib.buttons.joystickbutton import JoystickButton

#*********Robot-Side Initialization***************
class Right_Motors():
    def __init__(self):
        #Initialize Right motors
        right_motors = []
        right_motors.append(wpilib.VictorSP(3))
        right_motors.append(wpilib.VictorSP(4))
        right_motors.append(wpilib.VictorSP(5))