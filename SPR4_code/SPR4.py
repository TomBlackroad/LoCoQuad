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
import os

from random import randint
from camera import Cam
from robot import Robot
from servo_hat_driver import PCA9685
from IMU import IMU


class SPR4(Robot):
    def __init__(self):        
        super(SPR4, self).__init__("/home/pi/SPR4/SPR4_code/SPR4.botfile.txt")
        #Brain method --- conscience!!!!
        if(len(sys.argv)==2):
            print("EXECUTING TEST OF MOVEMENT", str(sys.argv[1])) 
            while True:
                super(SPR4,self).executeMove(str(sys.argv[1]), 1)
        else: 
            while True:
                self.generalFSM(self.state)


#=============================================================================
# GENERAL FSM
#=============================================================================
    def generalFSM(self, state):
        states_list = {
            0 : self.INIT,
            1 : self.REST,
            2 : self.EXPLORE,
            3 : self.SHOWOFF,
            4 : self.PHOTO,
        }
        func = states_list.get(state, lambda:None)
        return func()

#=============================================================================
# INIT STATE
#=============================================================================
    def INIT(self):
        print("CURRENT STATE: INIT")
        # use Raspberry Pi board pin numbers
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(mbl_bots.TRIG, GPIO.OUT)
        GPIO.setup(mbl_bots.ECHO, GPIO.IN)
        self.lastIMU = [0.0,0.0,0.0,0.0,0.0,0.0]
        self.currentIMU = [0.0,0.0,0.0,0.0,0.0,0.0]
        self.camera = Cam()
        self.imu = IMU(self.bus)
        self.distance = -1
        signal.signal(signal.SIGINT, self.close)
        self.state = mbl_bots.REST
        time.sleep(1)

#=============================================================================
# REST STATE
#=============================================================================
    def REST(self):
        print("CURRENT STATE: REST")
        start_time = time.time()
        while ((time.time()-start_time)<20):
            if(super(SPR4,self).detectCatch(self.imu)):
                for i in range(5):
                    super(SPR4,self).shake()
                break
            else:
                time.sleep(0.5)
        time.sleep(1)
        self.state = mbl_bots.EXPLORE

#=============================================================================
# EXPLORE STATE & FSM
#=============================================================================
    def exploreFSM(self, state):
        substates_explorelist = {
            0 : self.exploreGetData,
            1 : self.exploreProcessData,
            2 : self.exploreMove,
            3 : self.exploreReconTurn,
        }
        func = substates_explorelist.get(state, lambda:None)
        return func()

    def EXPLORE(self):
        print("CURRENT STATE: EXPLORE")
        super(SPR4,self).stand()
        #EXPLORING FiniteStateMachine
        while(self.state == mbl_bots.EXPLORE):
            self.exploreFSM()
        

    def exploreGetData(self):
        self.distance = utils.getDistance()
        self.lastIMU = self.currentIMU
        self.currentIMU = self.imu.getImuRawData()

        self.exploreState = mbl_bots.PROCESSDATA

    def exploreProcessData(self):
        if(self.distance < 5):
            self.movesCode = mbl_bots.WB
        elif(self.distance > 15):
            self.movesCode = mbl_bots.WF
        else:
            if(randint(0,1) == 1): 
                self.movesCode = mbl_bots.TR
            else: 
                self.movesCode = mbl_bots.TL

        if(randint(0,5)>1):
            self.exploreState = mbl_bots.MOVEMENT
        else:
            self.exploreState = mbl_bots.GETDATA
            self.state = mbl_bots.SHOWOFF

    def exploreMove(self):
        super(SPR4,self).move(self.movesCode)
        self.exploreState = mbl_bots.GETDATA

    def exploreReconTurn(self):
        print("Not implemented...")
        





#=============================================================================
# SHOW OFF STATE
#=============================================================================
    def SHOWOFF(self):
        print("CURRENT STATE: SHOWOFF")
        #SHOWOFF METHODS
        super(SPR4,self).swing()
        super(SPR4,self).sayHello()
        self.state = mbl_bots.PHOTO

#=============================================================================
# PHOTO STATE
#=============================================================================    
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
