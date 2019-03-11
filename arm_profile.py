# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 17:04:19 2019

@author: noahm
"""
import matplotlib.pyplot as plt

class Arm_Profile():
    def __init__(self,total_ticks,angle_max,angle_desired, max_accel, min_decel):
        tick_displacement = self.angle_to_ticks(angle_max, angle_desired, total_ticks)
        self.vp = [318.0 for i in range(tick_displacement)]
        self.x_axis_ticks = []
        for i in range(tick_displacement):
            self.x_axis_ticks.append(i)
        self.max_accel = max_accel
        self.min_decel = min_decel
    
    def angle_to_ticks(self, angle_max, angle_desired, total_ticks):
        proportion = angle_desired/angle_max
        tick_displacement = int(proportion*total_ticks)
        return tick_displacement
    
    def forward_accel(self, feed_forward):
        self.vp[0] = feed_forward
        for i in range(1,len(self.vp),1):
            self.vp[i] = min(self.vp[i],(self.vp[i-1]+self.max_accel))
            
    def backwards_accel(self, feed_backward):
        self.vp[-1] = feed_backward
        for i in range(len(self.vp)-2,0,-1):
            self.vp[i] = min(self.vp[i],(self.vp[i+1]+self.min_decel))
            
    def make_profile(self):
        self.forward_accel(75)
        self.backwards_accel(0)
            
    def plot(self):
        plt.plot(self.x_axis_ticks, self.vp)
        plt.show
        

#profile = Arm_Profile(1000, 140, 100, 0.7, 0.7)
#profile.make_profile()

#profile.plot()