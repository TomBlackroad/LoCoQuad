from time import sleep
from picamera import PiCamera
import datetime

class Cam(object):
	def __init__(self):
		self.camera = PiCamera()
		self.camera.resolution = (640, 480)
		#self.camera.rotation = 180
	
	def takePic(self):
		self.camera.start_preview()
		sleep(2)
		filename = "/home/pi/LoCoQuad/Code/Captures/" + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S.jpg')
		print(filename)
		self.camera.capture(filename)
		self.camera.stop_preview()

	def startVideo(self):
		filename = "/home/pi/LoCoQuad/Code/Captures/" + datetime.datetime.now().strftime('%Y-%m-%d--%H-%M-%S.h264')
		print(filename)
		self.camera.start_recording(filename)

	def endVideo(self):
		self.camera.stop_recording()
		