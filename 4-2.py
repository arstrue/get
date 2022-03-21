
import RPi.GPIO as gpio
from time import sleep
from threading import Thread

gpio.setmode(gpio.BCM)

dac = [26,19,13,6,5,11,9,10]

gpio.setup(dac, gpio.OUT)

def dec_to_bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

T = 1.

flag_1 = False
flag_2 = False

def Triangle():
    global flag_1
    global flag_2
    global T

    try:
        while not flag_1:
            ampl = 1
            t = T / 256

            T1 = T

            while(ampl < 255):
                gpio.output(dac, dec_to_bin(ampl))
                sleep(t)
                if T1 != T:
                    break

                ampl += 1

    finally:
        flag_2 = True



def ParseT(str):
    global T
    
    if (str.find("T ") == -1):
        return

    try:
        num = float(str[2:])
    except ValueError:
        print("Неизвестная команда")
    else:
        T = num

Thread(target = Triangle).start()

try:
    while (True):

        buf = input("Введите команду:\n")

        if (buf == "exit"):
            break

        ParseT(buf)

        continue
        
finally:
    flag_1 = True

    while (not flag_2):
        sleep(1)

    gpio.output(dac, 0)
    gpio.cleanup()
