# vim: set sw=4 sts=4 fileencoding=utf-8:
class Pid_Loop():
    def __init__():
        print(" Init ")
        self.kp = 1.0 
        self.ki = 1.0
        self.kd = 1.0
        
        #PID equation variables
        current_velocity_left = 0.0
        current_velocity_right = 0.0
        
        self.integral_value_filter = 100.0 #set threshold velocity error for accumulating integral values
        
        self.error_total_left = 0.0
        self.error_total_right = 0.0
        
        self.error_previous_left = 0.0
        self.error_previous_right = 0.0
        
        proportion_left = 0.0
        proportion_right = 0.0
        integral_left = 0.0
        integral_right = 0.0
        derivative_left = 0.0
        derivative_right = 0.0
        
    def get_error(self, side, encoder_val):
        print("Error " + str(side))
        error = abs(encoder_val) - 100
        return error
        
    def set_total_error(self, error):
        if error < self.integral_value_filter and error != 0:
            total_error += error
        else:
            total_error  = 0
            
    ### I think this should say max_error = 50/self.ki and then do a check_max_error or something
    def set_max_error(self, error):
        # Max error is 50 / self.ki
        if total_error > 50/self.ki:
                total_error = 50/self.ki
        return total_error
        
    
