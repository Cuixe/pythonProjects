class LedController:

    def __init__(self):
        self.__leds = []

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

    def getNumberOfLeds(self):
        return len(self.__leds)