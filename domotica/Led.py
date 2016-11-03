import RPi.GPIO as GPIO

class Led:
    def __init__(self, ledNumber, pin):
        self.__pin = pin
        self.ledNumbre = ledNumber
        GPIO.setup(self.__pin, GPIO.OUT)

    def turnOn(self):
        GPIO.output(self.__pin, GPIO.HIGH)

    def turnOff(self):
        GPIO.output(self.__pin, GPIO.LOW)
