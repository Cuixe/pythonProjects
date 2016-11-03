import LedEffects
import sys

class LedsOperation:

    CONTROLLER = LedEffects()

    def __init__(self, args):
        self.operation = args[1]
        if len(args) == 2:
            self.option = 1
        else:
            self.option = int(args[2])

    def execute(self):
        ejecutions = 0
        if self.operation == 'serie':
            while ejecutions < self.option:
                self.CONTROLLER.rightToLeft()
                ejecutions += 1
        elif self.operation == 'inv':
            while ejecutions < self.option:
                self.CONTROLLER.leftToRight()
                ejecutions += 1
        elif self.operation == 'kit':
            while ejecutions < self.option:
                self.CONTROLLER.rightToLeft()
                self.CONTROLLER.leftToRight()
                ejecutions += 1
        elif self.operation == 'all':
            if self.option == 1:
                self.CONTROLLER.turnAllOn()
            else:
                self.CONTROLLER.turnAllOff()
        else:
            if self.option == 1:
                self.CONTROLLER.turnOnLed(int(self.operation))
            else:
                self.CONTROLLER.turnOffLed(int(self.operation))
