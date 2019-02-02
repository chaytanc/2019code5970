# vim: set sw=4 noet ts=4 fileencoding=utf-8:

class Pid_Loop():
	def __init__():
		print(" Init ")
		self.kp = 1.0
		self.ki = 1.0
		self.kd = 0.0

		###is self.error necessary?
		self.error = 0

		###ask loli about max_error
		self.max_error = 50/self.ki

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

	def set_total_error(self, error, total_error):
		if error < self.integral_value_filter and error != 0:
			total_error += error
		else:
			total_error  = 0

		return total_error

	### I think this should say max_error = 50/self.ki and then do a
		# check_max_error or something
	def set_max_error(self, error, total_error):
		# Max error is 50 / self.ki
		if total_error > self.max_error:
			total_error = self.max_error

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

	def set_derivative(self, error, kd=1, previous_error=None):
		if previous_error is None:
			previous_error = 0

		if kd is None:
			kd = 0

		if error == 0:
			derivative = 0
		else:
			derivative = error - previous_error * kd

		return derivative

	def get_velocity(self, power_state, proportion, integral, derivative):
		if power_state == off:
			velocity = 0
		else:
		   velocity = proportion + integral + derivative

		return velocity

def do_pid_loop():
	# Get inputs for PID (encoder stuff)

	if self.auto_loop_counter < 300:
		
		# PID loop for target velocity on each side of drivetrain in auto
		# Input: target pathway (Noah code)
		pid = Pid_Loop()	
		previous_error = self.error 
		self.error = pid.get_error()
		self.total_error = pid.set_total_error(self.error, self.total_error)
		proportion = pid.set_proportion()
		max_error = pid.set_max_error()
		integral = pid.set_integral()
		derivative = pid.set_derivative(self.error, self.kd, previous_error)
		###right_velocity = pid.get_velocity()
				
		# Outputs for PID
	
		# set motor speed to PID outputs 

		time.sleep(0.2)
		  
	else:
		# set drive motors to zero if auto counter is done
		return None

	self.auto_loop_counter +=1
	# Why is this necessary?
	data = wpilib.DriverStation.getInstance().getGameSpecificMessage()



