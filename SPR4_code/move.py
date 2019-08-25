class Movement(object):
    """docstring for Movement"""
    def __init__(self, *args):
        super(Movement, self).__init__()
        self.actuator = args[0][0]
        self.pos = int(args[0][1])
