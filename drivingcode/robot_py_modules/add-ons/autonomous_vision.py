import wpilib
from wpilib.buttons.joystickbutton import JoystickButton
import sys
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules')

from variable_declarations import VariableDec    #Assign variables for encoders, motors, pistons etc. to use in robot.py and RobotPyModules 

import sys

#sys.path.append('./robot_py_modules/pneumatics') #Linux RobotPyModules path
sys.path.append('C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/drivingcode/robot_py_modules') #Windows RobotPyModules path
import autonomous_movement

#sys.path.insert(0, here + '/../vision')
#Windows path
#sys.path.insert(0,"C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/vision/tcp")
#import socket
#import json
#from time import sleep
#from server import parse, decode_json
#import re
#import argparse

class AutoVision(VariableDec):
    '''
    Control vision for better autonomous movement [DISABLED]
    '''
    
    def find_tape(self):
        '''
        self.TCP_IP = '10.59.70.12'
        self.TCP_PORT = 5005
        self.BUFFER_SIZE = 1024
        debug = False
        #parser = argparse.ArgumentParser(description="Beavertronics Jetson TX1 client")

        #parser.add_argument('-d', '--debug', action='store_true')
        #parser.add_argument('--sim', action='store_true')
        #print(sys.argv)
        #args = parser.parse_args()
        #if args.sim:
            #sys.argv=['robot.py', 'sim']

        if debug:
        #    print("Connecting to server on localhost...")
        #    self.TCP_IP = '127.0.0.1'

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect((self.TCP_IP, self.TCP_PORT))
            #print("We did it. Connection Hooray!")

        except:
            #print(e)
            print("no connection to jetson")
            return -1

        #if debug:
        #    print("Connection to local host established")
        while self.Gyroo.getAngle()<=360:#im assuming it's going to count up from 0 to 360
            self.setDriveMotors(-.25, -.25)
            deg,asmith,dist= self.distance_to_tape(s)
            if dist != -1:
                self.setDriveMotors(0, 0)
                return deg,asmith,dist
                break
        self.setDriveMotors(0, 0)
        return -1
        '''

    def distance_to_tape(self, s):
        debug = False
        #lolly's code here
        #Jetson path
        here = os.path.dirname(os.path.realpath(__file__))
        sys.path.insert(0, here + '/../../vision/tcp')

        #Windows path
        #sys.path.insert(0,"C:/Users/Beavertronics/Desktop/2018Workstation/2018code5970/vision/tcp")
        #import socket
        #import json
        #from time import sleep
        #from server import parse, decode_json
        #import re
        #import argparse

        self.PY2 = sys.version_info[0] == 2

        self.MSG_DEFAULT = "shutdown:" + json.dumps({}, ensure_ascii=False)
        self.LOC_DEFAULT = "locate_tape:" + json.dumps({}, ensure_ascii=False)
        self.RESET_DEFAULT = "reset_tape:"  + json.dumps({}, ensure_ascii=False)
        self.DEBUG_ON_DEFAULT = "debug_on:"  + json.dumps({}, ensure_ascii=False)
        self.DEBUG_DEFAULT = "debug_on:" + json.dumps({'filename':'/tmp/debugout'}, ensure_ascii=False)


        try:

            if self.PY2:
                s.send(self.RESET_DEFAULT)
            else:
                s.send(bytes(self.RESET_DEFAULT, 'utf-8'))

            self.cmd, self.json_data = parse(s.recv(self.BUFFER_SIZE))
            #if debug:
            #print("Got json_data: <" + self.json_data.decode('utf-8') + ">")
            #print("got here 201")
            while 1:
                sleep(0.1)
                if self.PY2:
                    s.send(self.LOC_DEFAULT)
                else:
                    s.send(bytes(self.LOC_DEFAULT, 'utf-8'))

                self.cmd, self.json_data = parse(s.recv(self.BUFFER_SIZE))
                print(self.json_data)
                if self.PY2:
                    self.tmp = self.json_data
                else:
                    self.tmp = self.json_data.decode('utf-8')
                    
                self.degrees, self.azim, self.distance = decode_json(self.tmp)
                return self.degrees, self.azim, self.distance
                #print("client received loc data: <"+ str(self.degrees) + " " + str(self.azim) + " " + str(self.distance) + ">")
        #KeyboardInterrupt is Ctrl-C
        except KeyboardInterrupt:
            print('interrupted')

        s.send(MSG_DEFAULT)
        self.json_data = s.recv(BUFFER_SIZE)
        s.close()

        if self.PY2:
            self.tmp = self.json_data
        else:
            self.tmp = self.json_data.decode('utf-8')
        print("client received shutdown data:" + self.tmp)