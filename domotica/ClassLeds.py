import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

class Led:
	def __init__(self, pin, ledNumber) :
		self.__pin = pin
		self.ledNumber = ledNumber
		GPIO.setup(self.__pin, GPIO.OUT)

	def turnOn(self):
		GPIO.output(self.__pin, GPIO.HIGH)

	def turnOff(self):
		GPIO.output(self.__pin, GPIO.LOW)

class LedsController:
	LEDS = [Led(14, 1), Led(15, 2), Led(18, 3), Led(23, 4), Led(24, 5), Led(25, 6), Led(8, 7), Led(7, 8)]

	def getLed(self, ledNumber) :
		for led in self.LEDS :
			if led.ledNumber == ledNumber :
				return led
		return

	def turnOnLed(self, ledNumber) :
		led = self.getLed(ledNumber)
		led.turnOn()
		return

	def turnOffLed(self, ledNumber) :
		led = self.getLed(ledNumber)
		led.turnOff()
		return

	def turnAllOn(self) :
		for led in self.LEDS :
			led.turnOn()
		return

	def turnAllOff(self) :
		for led in self.LEDS :
			led.turnOff()
		return
	
	def serieLeftToRight(self) :
		self.turnAllOff()
		numberLed = 1
		while (numberLed <= len(self.LEDS)) :
			led = self.getLed(numberLed)
			led.turnOn()
			time.sleep(.25)
			led.turnOff()
			numberLed += 1

	def serieRightToLeft(self) :
		self.turnAllOff()
		numberLed = len(self.LEDS)
		while (numberLed > 0) :
			led = self.getLed(numberLed)
			led.turnOn()
			time.sleep(.25)
			led.turnOff()
			numberLed -= 1

class Operator:

	CONTROLLER = LedsController()

	def __init__(self, args) :
		self.operation = args[1] 
		if len(args) == 2 :
			self.option = 1
		else :
			self.option = int(args[2])

	def execute(self) :
		counter = 0
		if self.operation == 'serie' :
			while(counter < self.option):
				self.CONTROLLER.serieRightToLeft()
				counter += 1
		elif self.operation == 'inv' :
			while(counter < self.option):
				self.CONTROLLER.serieLeftToRight()
				counter += 1
		elif self.operation == 'kit' :
			while(counter < self.option):
				self.CONTROLLER.serieRightToLeft()
				self.CONTROLLER.serieLeftToRight()
				counter += 1
		elif self.operation == 'all' :
			if self.option == 1:
				self.CONTROLLER.turnAllOn()
			else:
				self.CONTROLLER.turnAllOff()
		else :
			if self.option == 1:
				self.CONTROLLER.turnOnLed(int(self.operation))
			else:
				self.CONTROLLER.turnOffLed(int(self.operation))


operator = Operator(sys.argv)
operator.execute()