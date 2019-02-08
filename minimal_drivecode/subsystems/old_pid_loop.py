# vim: set sw=4 noet ts=4 fileencoding=utf-8:
import wpilib.command

class Pid_Loop(Subsytem):
	def __init__():
		print(" Init ")
		self.kp = 1.0
		self.ki = 1.0
		self.kd = 0.0

		###is self.error necessary?
		self.error = 0

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

	def set_max_error(self, ki):
		max_error = 50 / ki
		return max_error

	# Uses max error to redefine total_error
	def new_total_error(self, error, max_error, total_error):
		if total_error > max_error:
			total_error = max_error
		return total_error

	#put experimental default for kp etc
	def set_proportion(self, error, kp=1): 
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
			kd = 1

		if error == 0:
			derivative = 0
		else:
			derivative = error - previous_error * kd

		return derivative

	def get_velocity(self, power_state, proportion, integral, derivative):
		### Don't have a powerstate thing yet. probably accesible through wpilib
		### class function
		if power_state == off:
			velocity = 0
		else:
		   velocity = proportion + integral + derivative

		return velocity

def do_pid_loop(side, encoder_val, error, total_error, kp, ki, kd):
	# Get inputs for PID (encoder stuff)

	if self.auto_loop_counter < 300:
		
		# PID loop for target velocity on each side of drivetrain in auto
		# Input: target pathway (Noah code)
		# OR Input: Target arm velocity
		pid = Pid_Loop()	
		previous_error = self.error 
		self.error = pid.get_error(side, encoder_val)
		self.total_error = pid.set_total_error(error, total_error)
		max_error = pid.set_max_error(ki)
		new_total_error = pid.new_total_error(error, max_error, total_error)
		kp = pid.kp
		proportion = pid.set_proportion(error, kp)
		ki = pid.ki
		integral = pid.set_integral(error, ki)
		kd = pid.kd
		derivative = pid.set_derivative(error, kd, previous_error)
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



