# -*- coding: utf-8 -*-
"""
Created on Tue Feb 26 23:45:40 2019

@author: noahm
"""

class Arm_Position():
        
    def __init__(self, max_ticks):
        """ Gets encoder position while accounting for error
        at limit switches """
        self.arm_min_or_max = 0
        self.max_ticks = max_ticks
        self.last_encoder = 0
        
    def forward_limit(self, encoder_value):
        self.arm_min_or_max = 0
        self.last_encoder = encoder_value
        
    def rearward_limit(self, encoder_value):
        self.arm_min_or_max = self.max_ticks
        self.last_encoder = encoder_value
        
    def position(self, encoder_value):
        current_error = self.arm_min_or_max - self.last_encoder
        current_pos = encoder_value - current_error
        return current_pos