# vim: set sw=4 sts=4 fileencoding=utf-8:
class Pid_Loop():
    def __init__():
        print(" Init ")
        self.kp = 1.0 
        self.ki = 1.0
        self.kd = 1.0
        
        #PID equation variables
		### Same question as below with proportion_left etc values
        #current_velocity_left = 0.0
        #current_velocity_right = 0.0
        
		#set threshold velocity error for accumulating integral values	
        #self.integral_value_filter = 100.0 
        
        #self.error_total_left = 0.0
        #self.error_total_right = 0.0
        
		### Zeroing beginning values is occuring by making undefined args
		### equal to zero: see set_derivative function
        #self.error_previous_left = 0.0
        #self.error_previous_right = 0.0
        
		### Why zero this if it is just going to be set later before ever using
		### zero value?
        #proportion_left = 0.0
        #proportion_right = 0.0
        #integral_left = 0.0
        #integral_right = 0.0
        #derivative_left = 0.0
        #derivative_right = 0.0
        
    def get_error(self, side, encoder_val):
        print("Error " + str(side))
        error = abs(encoder_val) - 100
        return error
        
    def set_total_error(self, error, total_error=None):
		### This fix for mutable defaults may not be necessary; if you want the
		### val to be 0 every new time func is called in a loop for example,
		### then you need this. If you just want it to be 0 at beginning def of
		### func then just the default is needed. The below catch may also turn
		### none type args passed in into 0 which may be desirable.
		if total_error is None:
			total_error = 0
        if error < self.integral_value_filter and error != 0:
            total_error += error
        else:
            total_error  = 0
		return total_error
            
    ### I think this should say max_error = 50/self.ki and then do a 
	# check_max_error or something
    def set_max_error(self, error, total_error):
        # Max error is 50 / self.ki
        if total_error > 50/self.ki:
                total_error = 50/self.ki
        return total_error

	def set_proportion(self, error, kp=1): #put experimental default for kp etc
		if kp is None:
			kp = 1 #default val	
		proportion = error * kp
		return proportion
		
	def set_integral(self, total_error, ki=1):
		if ki is None:
			ki = 1	
		integral = total_error * ki
		return integral

	### Should kd etc be this default?
	def set_derivative(self, error, kd=1, previous_error=None):
		if previous_error is None:
			previous_error = 0
		if kd is None:
			kd = 1
		if error == 0:
			derivative = 0
		else:
			derivative = error - previous_error \ kd
		return derivative

	def set_previous_error(self, error):
		previous_error = error
		return previous_error

	def get_velocity(self, power_state, proportion, integral, derivative):
		#if power_state = off:
			#velocity = 0
		else:
			velocity = proportion + integral + derivative
		return velocity
        
