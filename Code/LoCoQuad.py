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


class LoCoQuad(Robot):
    def __init__(self):        
        super(LoCoQuad, self).__init__("/home/pi/LoCoQuad/Code/LoCoQuad.botfile.txt")
        #Brain method --- conscience!!!!
        if(len(sys.argv)==2):
            print("EXECUTING TEST OF MOVEMENT", str(sys.argv[1])) 
            while True:
                super(LoCoQuad,self).executeMove(str(sys.argv[1]), 1)
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
        #Distance Sensor Pins SetUp
        #GPIO.setup(mbl_bots.TRIG, GPIO.OUT)
        #GPIO.setup(mbl_bots.ECHO, GPIO.IN)
        self.lastIMU = [0.0,0.0,0.0,0.0,0.0,0.0]
        self.currentIMU = [0.0,0.0,0.0,0.0,0.0,0.0]
        self.camera = Cam()
        self.imu = IMU(self.bus)
        #self.distance = -1
        signal.signal(signal.SIGINT, self.close)
        self.state = mbl_bots.REST
        time.sleep(1)




#=============================================================================
# REST STATE
#=============================================================================
    def REST(self):
        print("CURRENT STATE: REST")
        start_time = time.time()
        while ((time.time()-start_time)<45):
            if(super(LoCoQuad,self).detectCatch(self.imu)):
                for i in range(3):
                    super(LoCoQuad,self).shake()
                break
            else:
                time.sleep(0.2)
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
        super(LoCoQuad,self).flat()
        time.sleep(1)
        super(LoCoQuad,self).stand()
        #EXPLORING FiniteStateMachine
        while(self.state == mbl_bots.EXPLORE):
            self.exploreFSM(self.exploreState)
        

    def exploreGetData(self):
        print("CURRENT STATE: EXPLORE")
        print("CURRENT SUBSTATE: DATA ACQUISITION")
        self.distance = utils.getDistance()
        self.lastIMU = self.currentIMU
        self.currentIMU = self.imu.getImuRawData()
        self.exploreState = mbl_bots.PROCESSDATA

    def exploreProcessData(self):
        print("CURRENT STATE: EXPLORE")
        print("CURRENT SUBSTATE: DATA PROCESSING")
        time.sleep(3)
        #if(self.distance < 5):
        #    self.movesCode = mbl_bots.WB
        #elif(self.distance > 15):
        #    self.movesCode = mbl_bots.WF
        #else:
            #if(randint(0,1) == 1): 
            #self.movesCode = mbl_bots.TR
            #else: 
            #    self.movesCode = mbl_bots.TL
        
        self.exploreState = mbl_bots.MOVE

        # if(randint(0,5)>1):
        #     self.exploreState = mbl_bots.MOVE
        # else:
        #     self.exploreState = mbl_bots.GETDATA
        #     self.state = mbl_bots.SHOWOFF

    def exploreMove(self):
        print("CURRENT STATE: EXPLORE")
        print("CURRENT SUBSTATE: MOVING")
        #super(LoCoQuad,self).move(self.movesCode)
        #super(LoCoQuad,self).move(self.movesCode)
        self.camera.startVideo()
        start_time = time.time()
        while ((time.time()-start_time)<20):
            super(LoCoQuad,self).walkFront()
        self.camera.endVideo()
        time.sleep(10)    
        #pose_count = 0
        # while ((time.time()-start_time)<60):
        #     if(super(LoCoQuad,self).isBalanced(self.imu)):
        #         super(LoCoQuad,self).balancePos(pose_count)
        #     else:
        #         super(LoCoQuad,self).balancePos(pose_count)
        #     if (pose_count >= 11):
        #         pose_count = 0 
        #     else:    
        #         pose_count = pose_count + 1
        #     time.sleep(0.5)
        # super(LoCoQuad,self).stand()
        # time.sleep(3)
        # super(LoCoQuad,self).walkFront()
        # super(LoCoQuad,self).walkFront()
        # super(LoCoQuad,self).walkFront()
        # super(LoCoQuad,self).walkFront()
        self.exploreState = mbl_bots.GETDATA

    def exploreReconTurn(self):
        print("Not implemented...")
        





#=============================================================================
# SHOW OFF STATE
#=============================================================================
    def SHOWOFF(self):
        print("CURRENT STATE: SHOWOFF")
        #SHOWOFF METHODS
        super(LoCoQuad,self).swing()
        super(LoCoQuad,self).sayHello()
        self.state = mbl_bots.PHOTO

#=============================================================================
# PHOTO STATE
#=============================================================================    
    def PHOTO(self):
        print("CURRENT STATE: PHOTO")
        super(LoCoQuad,self).cameraPose()
        self.camera.takePic()
        super(LoCoQuad,self).stand()
        self.state = mbl_bots.EXPLORE



    def close(self, signal, frame):
        self.camera.close()
        print("\nTurning off LoCoQuad Activity...\n")
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
  LoCoQuad = LoCoQuad()
