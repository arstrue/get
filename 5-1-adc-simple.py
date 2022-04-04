import RPi.GPIO as gpio
from time import sleep 


gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
troyka = 17
comp = 4

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(comp, gpio.IN)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]


def adc():
            
    voltage = 0
    while (voltage < 256):
                
        gpio.output(dac, dec_to_bin(voltage))

        sleep(0.1)
                
        if (gpio.input(comp) == 0):
            print("Adc Volage = {:.2} v, volage code = {}".format(voltage / 256.0 * 3.3, voltage))
            break
                
        voltage += 1


try:
    adc()

finally:
    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
