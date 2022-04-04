import RPi.GPIO as gpio
from time import sleep 

gpio.setmode(gpio.BCM)

dac = [26, 19, 13, 6, 5, 11, 9, 10]
leds = [21,20,16,12,7,8,25,24]
troyka = 17
comp = 4

gpio.setup(dac, gpio.OUT)
gpio.setup(troyka, gpio.OUT, initial = 1)
gpio.setup(leds, gpio.OUT)
gpio.setup(comp, gpio.IN)

def dec_to_bin(num):
    return [int(bit) for bit in bin(num)[2:].zfill(8)]

def bin_to_dec(bits):
    dec = 0
    code = 1
    for i in range(7, -1, -1):
        dec += bits[i] * code
        code *= 2
    return dec

def adc():
    voltage = 8*[0]
    
    gpio.output(dac, 0)

    sleep(0.01)

    for step in range(0, 8):
        voltage[step] = 1

        gpio.output(dac[step], voltage[step])

        sleep(0.01)

        if (gpio.input(comp) == 0):
            voltage[step] = 0
            gpio.output(dac[step], voltage[step])

    for step in range(0, 8):
        gpio.output(leds[step], voltage[step])
        
    print(voltage)
    dec = bin_to_dec(voltage)
    return dec

try:
    while(True):
        sleep(0.1)
        dec = adc()
        print("Adc Volage = {:.3} v, volage code = {}".format(dec / 256.0 * 3.3, dec))

   
finally:

    gpio.output(dac, 0)
    gpio.output(troyka, 0)
    gpio.cleanup()
