class Sensor(object):
	"""docstring for Actuator"""
	def __init__(self, args):
		super(Sensor, self).__init__()
		self.id = args[0]
		self.name = args[1]
		self.type = args[2]
		self.adress = args[3]
                
    def printshow(self):
        print("This is Sensor: ", self.name)