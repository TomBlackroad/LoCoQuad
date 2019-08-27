#!/usr/bin/python
import RPi.GPIO as GPIO
import time
import math
import smbus
import sys
import utils
import logging
import mbl_bots
import signal

from random import randint
from camera import Cam
from robot import Robot
from servo_hat_driver import PCA9685

class SPR4(Robot):
    def __init__(self):
        super(SPR4, self).__init__("SPR4.botfile.txt")
        #Brain method --- conscience!!!!
        self.GFSM()

    def GFSM(self):
        while True:
            self.FSM(self.state)

    def FSM(self, state):
        states_list = {
            0 : self.INIT,
            1 : self.REST,
            2 : self.EXPLORE,
            3 : self.SHOWOFF,
            4 : self.PHOTO,
        }
        func = states_list.get(state, lambda:None)
        return func()

    def INIT(self):
        print("CURRENT STATE: INIT")
        # use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(mbl_bots.TRIG, GPIO.OUT)
        GPIO.setup(mbl_bots.ECHO, GPIO.IN)
        self.camera = Cam()
        self.distance = -1
        signal.signal(signal.SIGINT, self.close)
        self.state = mbl_bots.REST
        time.sleep(1)

    def REST(self):
        print("CURRENT STATE: REST")
        self.state = mbl_bots.EXPLORE
        time.sleep(1)

    def EXPLORE(self):
        print("CURRENT STATE: EXPLORE")
        #EXPLORING METHODS
        #self.explore_FSM()
        self.distance = utils.getDistance()
        super(SPR4,self).flat()
        time.sleep(1)
        start_time = time.time()
        while ((time.time()-start_time)<20):
            super(SPR4,self).walkFront(1)
        super(SPR4,self).stand()
        start_time = time.time()
        while ((time.time()-start_time)<20):
            if(randint(0,1) == 1): super(SPR4,self).turnRight(1)
            else: super(SPR4,self).turnLeft(1)  
        self.state = mbl_bots.SHOWOFF

    def SHOWOFF(self):
        print("CURRENT STATE: SHOWOFF")
        #SHOWOFF METHODS
        #self.showoff_FSM()
        super(SPR4,self).swing()
        super(SPR4,self).sayHello()
        self.state = mbl_bots.PHOTO
    
    def PHOTO(self):
        print("CURRENT STATE: PHOTO")
        super(SPR4,self).cameraPose()
        self.camera.takePic()
        super(SPR4,self).stand()
        self.state = mbl_bots.EXPLORE

    def close(self, signal, frame):
        print("\nTurning off SPR4 Activity...\n")
        GPIO.cleanup() 
        sys.exit(0)

    


#                                                             #     
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#            _____                    _____                   #
#           /\    \                  /\    \                  #
#          /::\    \                /::\    \                 #   
#         /::::\    \               \:::\    \                #  
#        /::::::\    \               \:::\    \               #   
#       /:::/\:::\    \               \:::\    \              #   
#      /:::/__\:::\    \               \:::\    \             #
#     /::::\   \:::\    \              /::::\    \            #     
#    /::::::\   \:::\    \    ____    /::::::\    \           #     
#   /:::/\:::\   \:::\    \  /\   \  /:::/\:::\    \          #  
#  /:::/  \:::\   \:::\____\/::\   \/:::/  \:::\____\         #   
#  \::/    \:::\  /:::/    /\:::\  /:::/    \::/    /         #       
#   \/____/ \:::\/:::/    /  \:::\/:::/    / \/____/          #       
#            \::::::/    /    \::::::/    /                   #         
#             \::::/    /      \::::/____/                    #     
#             /:::/    /        \:::\    \                    #     
#            /:::/    /          \:::\    \                   #     
#           /:::/    /            \:::\    \                  #    
#          /:::/    /              \:::\____\                 #  
#          \::/    /                \::/    /                 #  
#           \/____/                  \/____/                  #    
#                                                             #  
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#  ---------------------------------------------------------  #
#                                                             #   

if __name__=='__main__':
  SPR4 = SPR4()
