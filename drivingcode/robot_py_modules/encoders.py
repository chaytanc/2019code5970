#*********Robot-Side Initialization***************
    class Encoders():
        def __init__(self):
            #Initialize Encoders
            #Rcoder = wpilib.Encoder(2,3)
            Lcoder = wpilib.Encoder(0,1)
            Gcoder = wpilib.Encoder(4,5)
            Wcoder = wpilib.Encoder(2,3)