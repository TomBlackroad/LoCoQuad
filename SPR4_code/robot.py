#!/usr/bin/python
import time
import math
import smbus
import sys

from utils import Utils
from servo_hat_driver import PCA9685

class Robot():
	def __init__(self, file):
		self.file = file
		[self.actuators[], self.sensors[]] = Utils.file2bot(file, mbl_bots.ACC,)

