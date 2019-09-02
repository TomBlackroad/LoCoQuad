class Actuator(object):
    """docstring for Actuator"""
    def __init__(self, *args):
        super(Actuator, self).__init__()
        self.id = args[0][0]
        self.name = args[0][1]
        self.type = args[0][2]
        self.adress = args[0][3]
        self.center = int(args[0][4])
        self.min = int(args[0][5])
        self.max = int(args[0][6])
        self.parentid = args[0][7]
        self.sonid = args[0][8]
                
    def printshow(self):
        print("This is Actuator: ", self.name)