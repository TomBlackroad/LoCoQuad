#!/usr/bin/python
import time
import math
import smbus
import sys

from robot import Robot
from servo_hat_driver import PCA9685

class SPR4(Robot):
  """SPR4 spirit"""
  def __init__(self):
    super(SPR4, self).__init__("SPR4.botfile.txt")

    self.arise(0.5)


  def arise(self, behaviour):
    """
    """

  def walkFront(self, speed, rand):
    """
    """
  def walkBack(self, speed, rand):
    """
    """
  def walkRight(self, speed, rand):
    """
    """
  def walkLeft(self, speed, rand):
    """
    """


if __name__=='__main__':

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