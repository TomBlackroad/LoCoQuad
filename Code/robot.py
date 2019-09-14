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
		self.bus = smbus.SMBus(1)
		self.pwm = PCA9685(self.bus, 0x40, debug=False)
		self.pwm.setPWMFreq(50)
		#print("My name is: ", self.actuators[0].name)
		self.names_acc = [self.actuators[i].name for i in range(len(self.actuators))]
		self.names_sen = [self.sensors[i].name for i in range(len(self.sensors))]
		self.idx_acc = [i for i in range(len(self.actuators))]
		self.idx_sen = [i for i in range(len(self.sensors))]
		self.acc_dic = utils.genDictionary(self.names_acc, self.idx_acc)
		self.sen_dic = utils.genDictionary(self.names_sen, self.idx_sen)
		self.state = mbl_bots.INIT
		self.exploreState = mbl_bots.GETDATA
		self.movesCode = mbl_bots.NONE
		#print(self.acc_dic)

	def moveAcc(self,name,pos):
		poss = pos*mbl_bots.SCALE_ACC + mbl_bots.CNT_ACC
		if (poss > self.actuators[int(self.acc_dic[name])].max): poss = self.actuators[int(self.acc_dic[name])].max
		if (poss < self.actuators[int(self.acc_dic[name])].min): poss = self.actuators[int(self.acc_dic[name])].min
		self.pwm.setServoPulse(int(self.actuators[int(self.acc_dic[name])].adress), poss)
		#print('Moving ', name ,'to', poss )

	def executeMove(self,file,speed):
		moves = utils.file2move(file)
		for i in range(len(moves)):
			self.moveAcc(moves[i].actuator, moves[i].pos)
			if(moves[i].delay > 0.0):
				time.sleep(moves[i].delay*speed)

	def executeMoveOBO(self,file,speed,count,correction):
		moves = utils.file2move(file)
		if(count*2<=len(moves)):
			self.moveAcc(moves[count*2].actuator, moves[count*2].pos)
			self.moveAcc(moves[count*2+1].actuator, moves[count*2+1].pos)
			#if(moves[i].delay > 0.0):
			#	time.sleep(moves[i].delay*speed)

	def flat(self):
		print("LoCoQuad is Flat")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_flat.movefile.txt", 1)    

	def stand(self):
		print("LoCoQuad is Standing")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_stand.movefile.txt", 1)

	def walkFront(self, speed=1):
		print("LoCoQuad is Walking Forward")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_walkFront.movefile.txt", speed)

	def walkRight(self, speed=1):
		print("LoCoQuad is Walking Right")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_walkFront.movefile.txt", speed)
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_walkFront.movefile.txt", speed)

	def walkLeft(self, speed=1):
		print("LoCoQuad is Walking Left")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_walkFront.movefile.txt", speed)

	def walkBack(self, speed=1):
		print("LoCoQuad is Walking Backwards")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_walkBack.movefile.txt", speed)

	def turnRight(self, speed=1):
		print("LoCoQuad is Turning Right")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_turnRight.movefile.txt", speed)

	def turnLeft(self, speed=1):
		print("LoCoQuad is Turning Left")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_turnLeft.movefile.txt", speed)
	
	def sayHello(self):
		print("LoCoQuad is Saying Hi!")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_sayHello.movefile.txt", 1)

	def cameraPose(self):
		print("LoCoQuad ready to take Picture")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_cameraPose.movefile.txt", 1)

	def swing(self):
		print("LoCoQuad is Swinging")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_swing.movefile.txt", 1)	

	def shake(self):
		print("LoCoQuad is Shaking")
		self.executeMove("/home/pi/LoCoQuad/Code/LoCoQuad_shake.movefile.txt", 1)	

	def balancePos(self, count, correction=0):
		print("LoCoQuad is balancing")
		self.executeMoveOBO("/home/pi/LoCoQuad/Code/LoCoQuad_balance.movefile.txt", 1, count, correction)	


	def move(self, code):
		moves = {
        	1: self.walkFront,
        	2: self.walkBack,
        	3: self.walkRight,
        	4: self.walkLeft,
        	5: self.turnRight,
        	6: self.turnLeft,
        	7: self.flat,
        	8: self.stand,
    	}
		func = moves.get(code, lambda:None)
		return func()

	def detectCatch(self, imu):
		data = imu.getImuRawData()
		print(data)
		if(data[3] > 3 or data[4] > 3 or data[5] > 3): 
			print("ROBOT CATCHED...do something!!")
			return True
		else: 
			return False

	def isBalanced(self, imu):
		data = imu.getImuRawData()
		if(data[0] < 0.2 or data[1] < 0.2): 
			return True
		else: 
			return False
