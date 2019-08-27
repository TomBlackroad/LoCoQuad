import RPi.GPIO as GPIO
import time
import signal
import sys
import mbl_bots
import logging
from actuator import Actuator
from sensor import Sensor
from move import Movement

def file2bot(file, types):
    with open(file) as data:
        lines = [i.strip().split() for i in data]
    
    
    n_acc = int(lines[0][0])
    for i in range(n_acc):
        if(len(lines[i+1]) == mbl_bots.N_ACC_PARAM):
            actuators = [Actuator(lines[j+1]) for j in range(n_acc)]    
        else:
            logging.debug('The botfile is corrupted...fix it to obtain optimum results!')
    
    n_sen = int(lines[n_acc+1][0])
    for i in range(n_sen):
        print(len(lines[n_acc+i+1]))
        if(len(lines[n_acc+i+1]) == mbl_bots.N_SEN_PARAM):
            sensors = [Sensor(lines[n_acc+i+1]) for j in range(n_sen)]
        else:
            logging.debug('The botfile is corrupted...fix it to obtain optimum results!')


    if(types == mbl_bots.ACC):
        return (actuators)
    elif(types == mbl_bots.SEN):
        return (sensors)
    else:
        return (actuators, sensors)


def genDictionary(list1, list2):
    dic = {}
    if len(list2) == len(list1):
        for i in range(len(list1)):
            dic[list1[i]] = list2[i]
    return dic


def getDelay(speed):
    return speed/mbl_bots.SPEED_FACTOR


def file2move(file):
    with open(file) as data:
        lines = [i.strip().split() for i in data]

    for i in range(int(lines[0][0])):
        moves = [Movement(lines[j+1]) for j in range(int(lines[0][0]))]
    return moves


def getDistance():
    distance = -1.0
    buff = [0,0,0]
    for i in range(3):
        #try:
        # set Trigger to HIGH
        GPIO.output(mbl_bots.TRIG, True)
        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(mbl_bots.TRIG, False)

        startTime = time.time()
        stopTime = time.time()

        # save start time
        while 0 == GPIO.input(mbl_bots.ECHO):
            startTime = time.time()

        # save time of arrival
        while 1 == GPIO.input(mbl_bots.ECHO):
            stopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = stopTime - startTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        buff[i] = (TimeElapsed * 34300.0) / 2.0
        time.sleep(0.2)

        #except:
        #    print("Not able to get distance... something went wrong!!")
        #    return distance

    buff_avg = (buff[0]+buff[1]+buff[2])/3.0
    if buff_avg > 0.0: 
        distance = buff_avg
        print("Distance to nearest object is: %.1f cm" % distance)
    else:
        print("Not able to get distance...")
    return distance
        #print("Distance: %.1f cm" % distance)    