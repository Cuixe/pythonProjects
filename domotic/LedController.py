from Led import Led
import time


class LedController:

    def __init__(self):
        self.__leds = [
            Led(14),
            Led(15),
            Led(18),
            Led(23),
            Led(24),
            Led(25),
            Led(8),
            Led(7)
        ]

    def addLed(self, led):
        self.__leds.append(led)

    def getLed(self, led_number):
        for led in self.__leds:
            if led.ledNumber == led_number:
                return led
        return

    def turnAllOff(self):
        for led in self.__leds:
            led.turnOff()
        return

    def turnAllOn(self):
        for led in self.__leds:
            led.turnOn()
        return

    def leftToRight(self):
        self.turnAllOff()
        number_of_led = 1
        while number_of_led <= len(self.__leds):
            led = self.getLed(number_of_led)
            led.turnOn()
            time.sleep(.25)
            led.turnOff()
            number_of_led += 1

    def rightToLeft(self):
        self.turnAllOff()
        number_of_led = len(self.__leds)
        while number_of_led > 0:
            led = self.getLed(number_of_led)
            led.turnOn()
            time.sleep(.25)
            led.turnOff()
            number_of_led -= 1
