import RPi.GPIO as GPIO
import sys
import time

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

pins=[18, 23, 24, 14, 15, 25, 8]

def turnAllOn() :
	count = 0;
	while(count < len(pins)):
		turnOn(count-1)
		count += 1
	return

def turnAllOff() :
	count = 0;
	while(count < len(pins)):
		turnOff(count+1)
		count += 1
	return

def turnOn(led) :
	pin = pins[led-1]
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.HIGH)
	return

def turnOff(led):
	pin = pins[led-1]
	GPIO.setup(pin, GPIO.OUT)
	GPIO.output(pin, GPIO.LOW)
	return

def serie() :
	turnAllOff()
	count = 0;
	while(count < len(pins)):
		turnOn(count+1)
		time.sleep(.25)
		turnOff(count+1)
		count += 1

def inv() :
	turnAllOff()
	ciclos = 0
	count = len(pins)
	while (count > 0) :
		turnOn(count+1)
		time.sleep(.25)
		turnOff(count+1)
		count -= 1
		

def kit() :
	turnAllOff()
	serie()
	inv()

operacion = sys.argv[1]
if len(sys.argv) == 2 :
	option = 1
else :
	option = int(sys.argv[2])

if operacion == 'all':
	if sys.argv[2] == '1':
		turnAllOn()
	else:
		turnAllOff()
elif operacion == 'serie':
	ciclos = 0
	while (ciclos < option):
		serie()
		ciclos += 1
elif operacion == 'inv':
	ciclos = 0
	while (ciclos < option):
		inv()
		ciclos += 1
elif operacion == 'kit' :
	ciclos = 0
	while (ciclos < option):
		kit()
		ciclos += 1
elif len(sys.argv) != 3:
	print 'Parametros invalidos'
	sys.exit(1)
else:
	if option == 1:
		turnOn(int(operacion))
	else:
		turnOff(int(operacion))

