from LedController import LedController
from utils import Cleaner

class LedsOperation:

    def __init__(self, args):
        self.controller = LedController()
	self.cleaner = Cleaner()
        self.operation = args[1]
        if len(args) == 2:
            self.option = 1
        else:
            self.option = int(args[2])

    def execute(self):
        ejecutions = 0
        if self.operation == 'serie':
            while ejecutions < self.option:
                self.controller.rightToLeft()
                ejecutions += 1
        elif self.operation == 'inv':
            while ejecutions < self.option:
                self.controller.leftToRight()
                ejecutions += 1
        elif self.operation == 'kit':
            while ejecutions < self.option:
                self.controller.rightToLeft()
                self.controller.leftToRight()
                ejecutions += 1
        elif self.operation == 'all':
            if self.option == 1:
                self.controller.turnAllOn()
            else:
                self.controller.turnAllOff()
	elif self.operation == 'clean':
	    self.cleaner.clean_all()
        else:
            if self.option == 1:
                self.controller.turnOnLed(int(self.operation))
            else:
                self.controller.turnOffLed(int(self.operation))
