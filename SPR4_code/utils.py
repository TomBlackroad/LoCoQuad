import mbl_bots
import logging
from actuator import Actuator
from sensor import Sensor

def file2bot(file, types):
	with open(file) as data:
	    lines = [i.strip().split() for i in data]
    actuators = [Actuator(lines[i+1]) for i in range(lines[0]) if lengh(lines[i+1]) is 8]

n_acc = int(lines[0][0])
for i in range(n_acc):
    if(len(lines[i+1]) == mbl_bots.N_ACC_PARAM):
        actuators = [Actuator(lines[j+1]) for j in range(n_acc)]    
    else:
        logging.debug('The botfile is corrupted...fix it to obtain optimum results!')
    
n_sen = int(lines[n_acc+1][0])
for i in range(n_acc):
    if(len(lines[i+1]) == mbl_bots.N_SEN_PARAM):
        sensors = [Sensor(lines[n_acc+i+2]) for j in range(n_sen)]
    else:
        logging.debug('The botfile is corrupted...fix it to obtain optimum results!')




	if(types = mbl_bots.ACC):
		return (actuators)
	else if(types = mbl_bots.SEN):
		return (sensors)
	else:
		return (actuators, sensors)