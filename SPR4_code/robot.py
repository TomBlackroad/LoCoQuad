#!/usr/bin/python
import time
import math
import smbus
import sys
import utils
import mbl_bots
import logging


from servo_hat_driver import PCA9685


class Robot(object):
	def __init__(self, file):
		super(Robot, self).__init__()
		(self.actuators, self.sensors) = utils.file2bot(file, mbl_bots.BOTH)
		self.pwm = PCA9685(0x40, debug=False)
		self.pwm.setPWMFreq(50)
		print("My name is: ", self.actuators[0].name)
		self.names_acc = [self.actuators[i].name for i in range(len(self.actuators))]
		self.names_sen = [self.sensors[i].name for i in range(len(self.sensors))]
		self.idx_acc = [i for i in range(len(self.actuators))]
		self.idx_sen = [i for i in range(len(self.sensors))]
		self.acc_dic = utils.genDictionary(self.names_acc, self.idx_acc)
		self.sen_dic = utils.genDictionary(self.names_sen, self.idx_sen)
		self.state = mbl_bots.INIT
		print(self.acc_dic)

	def moveAcc(self,name,pos):
		poss = pos*mbl_bots.SCALE_ACC + mbl_bots.CNT_ACC
		if (poss > self.actuators[int(self.acc_dic[name])].max): poss = self.actuators[int(self.acc_dic[name])].max
		if (poss < self.actuators[int(self.acc_dic[name])].min): poss = self.actuators[int(self.acc_dic[name])].min
		self.pwm.setServoPulse(int(self.actuators[int(self.acc_dic[name])].adress), poss)
		print('Moving ', name ,'to', poss )

	def executeMove(self,file,speed):
		moves = utils.file2move(file)
		for i in range(len(moves)):
			self.moveAcc(moves[i].actuator, moves[i].pos)
			if(moves[i].delay > 0.0):
				time.sleep(moves[i].delay*speed)

	def flat(self):
		logging.debug("SPR4 is Flat")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_flat.movefile.txt", 1)    

	def stand(self):
		logging.debug("SPR4 is Standing")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_stand.movefile.txt", 1)

	def walkFront(self, speed):
		logging.debug("SPR4 is Walking Forward")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkFront.movefile.txt", speed)

	def walkBack(self, speed):
		logging.debug("SPR4 is Walking Backwards")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_walkBack.movefile.txt", speed)

	def turnRight(self, speed):
		logging.debug("SPR4 is Turning Right")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_turnRight.movefile.txt", speed)

	def turnLeft(self, speed):
		logging.debug("SPR4 is Turning Left")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_turnLeft.movefile.txt", speed)
	
	def sayHello(self):
		logging.debug("SPR4 is Saying Hi!")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_sayHello.movefile.txt", 1)

	def cameraPose(self):
		logging.debug("SPR4 ready to take Picture")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_cameraPose.movefile.txt", 1)

	def swing(self):
		logging.debug("SPR4 is Swinging")
		self.executeMove("/home/pi/SPR4/SPR4_code/SPR4_swing.movefile.txt", 1)		

