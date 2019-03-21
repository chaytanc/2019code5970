# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 12:09:25 2019

@author: noahm
"""

import arm_profile
import arm_position_counter


class Profile_Generator():

    def __init__(self,max_ticks,max_angle):
        """ Generates profile """
        self.apc = arm_position.Arm_Position(max_ticks)
        # Measure later
        self.max_ticks = max_ticks
        self.max_angle = max_angle
        
    def generate(self,encoder_value,end_angle):
        # Encoder value at the time of generating profile
        self.encoder_start = encoder_value
        # Needs to be changed to angle from ticks
        current_pos = self.apc.position(encoder_value)
        displacement_angle = end_angle - current_pos
        profile = arm_profile.Arm_Profile(
                self.max_ticks, self.max_angle, displacement_angle, 
                700, 700)
        profile.make_profile()
        self.profile = profile.vp
        
    def pick_motor_value(self,current_tick_count):
        profile_ticks = current_tick_count - self.encoder_start
        return self.profile[profile_ticks]
    
    