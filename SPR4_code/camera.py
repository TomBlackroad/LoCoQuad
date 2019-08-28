from time import sleep
from picamera import PiCamera
import datetime

class Cam(object):
	def __init__(self):
		self.camera = PiCamera()
		self.camera.resolution = (1024, 768)
		self.camera.rotation = 180
	
	def takePic(self):
		self.camera.start_preview()
		sleep(2)
		filename = "/home/pi/SPR4/SPR4_code/Captures/" + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S.jpg')
		print(filename)
		self.camera.capture(filename)
		self.camera.stop_preview()
