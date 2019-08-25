#!/usr/bin/python
import time
import math
import smbus
import sys
import utils
import logging

from robot import Robot
from servo_hat_driver import PCA9685

class SPR4(Robot):
  """SPR4 spirit"""
  def __init__(self):
    super(SPR4, self).__init__("SPR4.botfile.txt")
    self.home = 90
    self.arise(0.5)


  def arise(self, behaviour):
    time.sleep(2)
    start_time = time.time()
    while ((time.time()-start_time)<60):
      self.stand()
    start_time = time.time()
    while True:
      self.flat()
    

  def flat(self):
    logging.debug("SPR4 is standing")
    super(SPR4,self).executeMove("SPR4_flat.movefile.txt")    
    #super(SPR4,self).moveAcc("FSR", self.home)
    #super(SPR4,self).moveAcc("FSL", self.home)
    #super(SPR4,self).moveAcc("BSR", self.home)
    #super(SPR4,self).moveAcc("BSL", self.home)
    #super(SPR4,self).moveAcc("FLR", self.home)
    #super(SPR4,self).moveAcc("FLL", self.home)
    #super(SPR4,self).moveAcc("BLR", self.home)
    #super(SPR4,self).moveAcc("BLL", self.home)
    time.sleep(1)

  def stand(self):
    logging.debug("SPR4 is standing")
    super(SPR4,self).executeMove("SPR4_stand.movefile.txt")
    #super(SPR4,self).moveAcc("FSR", self.home)
    #super(SPR4,self).moveAcc("FSL", self.home)
    #super(SPR4,self).moveAcc("BSR", self.home)
    #super(SPR4,self).moveAcc("BSL", self.home)
    #super(SPR4,self).moveAcc("FLR", self.home-80)
    #super(SPR4,self).moveAcc("FLL", self.home+80)
    #super(SPR4,self).moveAcc("BLR", self.home+80)
    #super(SPR4,self).moveAcc("BLL", self.home-80)
    time.sleep(1) 

  def walkFront(self, speed, rand):
    ms = utils.getDelay(speed)
    logging.debug("SPR4 is Walking forward")
    print('SPR4 is walking forward...')

    super(SPR4,self).moveAcc('BLL', self.home + 50*rand)
    super(SPR4,self).moveAcc('FLR', self.home - 30*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("FSR", self.home - 45*rand)
    super(SPR4,self).moveAcc("BSR", self.home + 60*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("FLR", self.home - 80*rand)
    super(SPR4,self).moveAcc("BLL", self.home + 60*rand)
    super(SPR4,self).moveAcc("FLR", self.home - 80*rand)
    super(SPR4,self).moveAcc("BLL", self.home + 50*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("BSL", self.home + 30*rand)
    super(SPR4,self).moveAcc("FSR", self.home + 20*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("BLL", self.home + 60*rand)
    super(SPR4,self).moveAcc("FLL", self.home + 80*rand)
    super(SPR4,self).moveAcc("BLL", self.home + 20*rand)
    super(SPR4,self).moveAcc("FLL", self.home + 40*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("FSL", self.home + 60*rand)
    super(SPR4,self).moveAcc("BSL", self.home - 50*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("FLL", self.home + 70*rand)
    super(SPR4,self).moveAcc("BLR", self.home - 70*rand)
    super(SPR4,self).moveAcc("FLL", self.home + 40*rand)
    super(SPR4,self).moveAcc("BLR", self.home - 40*rand)
    time.sleep(ms)
    super(SPR4,self).moveAcc("BSR", self.home - 20*rand)
    super(SPR4,self).moveAcc("FSL", self.home)
    time.sleep(ms)
    super(SPR4,self).moveAcc("BLR", self.home - 50*rand)
    super(SPR4,self).moveAcc("FLL", self.home + 70*rand)
    time.sleep(ms)


#  def walkBack(self, speed, rand):
#    """
#    """
#  def walkRight(self, speed, rand):
#    """
#    """
#  def walkLeft(self, speed, rand):
#    """
#    """

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
  

"""
if __name__=='__main__':
  pwm = PCA9685(0x40, debug=True)
  pwm.setPWMFreq(50)
  while True:
    pwm.setServoPulse(0,1000)
    pwm.setServoPulse(2,1000)
    pwm.setServoPulse(4,1000)
    pwm.setServoPulse(6,1000)
    time.sleep(2)
    pwm.setServoPulse(1,1000)
    pwm.setServoPulse(3,1000)
    pwm.setServoPulse(5,1000)
    pwm.setServoPulse(7,1000)
    time.sleep(5)
    pwm.setServoPulse(0,2000)
    pwm.setServoPulse(2,2000)
    pwm.setServoPulse(4,2000)
    pwm.setServoPulse(6,2000)
    time.sleep(2)
    pwm.setServoPulse(1,2000)
    pwm.setServoPulse(3,2000)
    pwm.setServoPulse(5,2000)
    pwm.setServoPulse(7,1000)
    time.sleep(5)
    pwm.setServoPulse(0,1500)
    pwm.setServoPulse(2,1500)
    pwm.setServoPulse(4,1500)
    pwm.setServoPulse(6,1500)
    time.sleep(2)
    pwm.setServoPulse(1,1500)
    pwm.setServoPulse(3,1500)
    pwm.setServoPulse(5,1500)
    pwm.setServoPulse(7,1500)
    time.sleep(5)
    pwm.setServoPulse(0,1700)
    pwm.setServoPulse(2,1700)
    pwm.setServoPulse(4,1700)
    pwm.setServoPulse(6,1700)
    time.sleep(2)
    pwm.setServoPulse(1,1700)
    pwm.setServoPulse(3,1700)
    pwm.setServoPulse(5,1700)
    pwm.setServoPulse(7,1700)
    time.sleep(5)
   # setServoPulse(2,2500)
   # for i in range(500,2500,2):
   #   pwm.setServoPulse(int(sys.argv[1]),i)
   # for i in range(2500,500,-2):
   #   pwm.setServoPulse(int(sys.argv[1]),i)
"""
