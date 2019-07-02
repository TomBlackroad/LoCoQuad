#!/usr/bin/python
import time
import math
import smbus
import sys
import utils
import mbl_bots


from servo_hat_driver import PCA9685


class Robot(object):
	def __init__(self, file):
		super(Robot, self).__init__()
		(self.actuators, self.sensors) = utils.file2bot(file, mbl_bots.BOTH)
		self.pwm = PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)
		names_acc = [actuators[i].name for i in len(actuators)]
		names_sen = [sensors[i].name for i in len(sensors)]
		idx_acc = [i for i in len(actuators)]
		idx_sen = [i for i in len(sensors)]
		self.acc_dic = utils.genDictionary(name_acc, idx_acc)
		self.sen_dic = utils.genDictionary(name_sen, idx_sen)

	def moveAcc(self,adress,pos):
		poss = pos*mbl_bots.SCALE_ACC + mbl_bots.CNT_ACC
		if (poss > actuators[int(self.acc_dic[name])].max): poss = actuators[int(self.acc_dic[name])].max
		if (poss < actuators[int(self.acc_dic[name])].min): poss = actuators[int(self.acc_dic[name])].min
		self.pwm.setServoPulse(actuators[int(self.acc_dic[name])].adress, pos)


