# vim: set sw=4 sts=4 fileencoding=utf-8:
import wpilib

#*********Robot-Side Initialization***************
class Encoders():
    #Don't initialize variables in init if you need it as an attribute
    #def __init__(self):
    '''
        #Initialize Encoders
        Rcoder = wpilib.Encoder(2,3)
        Lcoder = wpilib.Encoder(0,1)
        Gcoder = wpilib.Encoder(4,5)
        #Wcoder = wpilib.Encoder(2,3)
    '''
    Rcoder = wpilib.Encoder(2,3)
    Lcoder = wpilib.Encoder(0,1)
    Gcoder = wpilib.Encoder(4,5)
