# vim: set sw=4 sts=4 fileencoding=utf-8:
class Wrist():

    
    def actuate_wrist(self, state):#must get maximum and minimum
            # Get max and min rotation of wrist so it yon't break 
            max_wrist = 90 # set low so it stops before it breaks at 100
            ### Is min necessary?
            min_wrist = 10 # set high so it stops before it breaks at 0
            ### where does direction come from? Should it be passed in? State is passed in but not used
            # If joystick pushed forward, make wrist actuate up
            if direction == "Forward":
                while self.encdrs.Wcoder.get() < max_wrist:
                    for motor in self.CubeIntakeL_motor:
                        motor.set(.25)
                for motor in self.CubeIntakeL_motor:
                        motor.set(0)
            # If joystick pulled, make wrist actuate down
            elif direction == "Backward":
                while self.encdrs.Wcoder.get() < max_wrist:
                    for motor in self.CubeIntakeL_motor:
                        motor.set(-.25)
                for motor in self.CubeIntakeL_motor:
                        motor.set(0)
