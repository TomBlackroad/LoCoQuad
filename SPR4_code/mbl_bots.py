#Actuators or Sensors
ACC = 0
SEN = 1
BOTH = 2

#Number of parameters that define an Actuator or a Sensor
N_ACC_PARAM = 9
N_SEN_PARAM = 4

#Factor for movemente speed scaling
SPEED_FACTOR = 10.0

#Scaling factor from angles to pulses
SCALE_ACC = 11
CNT_ACC = 500

#GENERAL FINITE STATE MACHINE
#States
INIT = 0
REST = 1
EXPLORE = 2
SHOWOFF = 3
PHOTO = 4

#EXPLORE FINITE STATE MACHINE
#States
GETDATA = 0
PROCESSDATA = 1
MOVE = 2

#MOVES CODES
NONE = 0
WF = 1
WB = 2
WR = 3
WL = 4
TR = 5
TL = 6
FLAT = 7
STAND = 8

# GPIO Pins
TRIG = 27
ECHO = 22

#IMU REGISTERS
#some MPU6050 Registers and their Address
PWR_MGMT_1 = 0x6B
SMPLRT_DIV = 0x19
CONFIG = 0x1A
GYRO_CONFIG = 0x1B
INT_ENABLE = 0x38
ACCEL_XOUT_H = 0x3B
ACCEL_YOUT_H = 0x3D
ACCEL_ZOUT_H = 0x3F
GYRO_XOUT_H = 0x43
GYRO_YOUT_H = 0x45
GYRO_ZOUT_H = 0x47