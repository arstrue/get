import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)
gpio.setup(23, gpio.OUT)

p = gpio.PWM(23, 1000)
p.start(0)

try:
    while(True):
        print("Введите число:")

        str = input()


        p.ChangeDutyCycle(float(str))

finally:
    gpio.cleanup()
