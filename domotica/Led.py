import RPi.GPIO as GPIO


class Led:

    ledNumber = 1

    def __init__(self, pin):
        self.__pin = pin
        self.ledNumber = Led.ledNumber
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)
        GPIO.setup(self.__pin, GPIO.OUT)
        Led.ledNumber += 1

    def turnOn(self):
        GPIO.output(self.__pin, GPIO.HIGH)

    def turnOff(self):
        GPIO.output(self.__pin, GPIO.LOW)
