import RPi.GPIO as GPIO
import Led
import LedController
import time

class LedEffect:

    def __init__(self):
        controller = LedController()
        controller.addLed(Led(1, 14))
        controller.addLed(Led(2, 15))
        controller.addLed(Led(3, 18))
        controller.addLed(Led(4, 23))
        controller.addLed(Led(5, 24))
        controller.addLed(Led(6, 25))
        controller.addLed(Led(7, 8))
        controller.addLed(Led(8, 7))
        self.__ledController = controller
        GPIO.setmode(GPIO.BCM)
        GPIO.setwarnings(False)

    def leftToRight(self):
        self.__ledController.turnAllOff()
        number_of_led = 1
        while number_of_led <= self.__ledController.getNumberOfLeds():
            led = self.__ledController.getLed(number_of_led);
            led.turnOn()
            time.sleep(.25)
            led.turnOff()
            number_of_led += 1

    def rightToLeft(self):
        self.turnAllOff()
        number_of_led = self.__ledController.getNumberOfLeds()
        while number_of_led > 0:
            led = self.__ledController.getLed(number_of_led)
            led.turnOn()
            time.sleep(.25)
            led.turnOff()
            number_of_led -= 1

    def turnOnLed(self, ledNumber):
        self.__ledController.getLed(ledNumber).turnOn()

    def turnOffLed(self, ledNumber):
        self.__ledController.getLed(ledNumber).turnOff()