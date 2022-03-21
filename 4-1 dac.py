import RPi.GPIO as gpio

gpio.setmode(gpio.BCM)

dac = [26,19,13,6,5,11,9,10]

gpio.setup(dac, gpio.OUT)

def dec_to_bin(n):
    return [int(bit) for bit in bin(n)[2:].zfill(8)]

def print_volt(n):
    print("Out voltage V = {:.3f} B".format(n/256.))

try:
    while(True):
        print("Введите число:")

        str = input()

        if(str == "exit"):
            break

        try:
            n = int(str)
        except ValueError:
            print("Ошибка ввода, введенная строка не является десятичным числом.", sep = ' ')
        
        else:
            if n < 0:
                print("Введите положительное значение.")
                continue

            if n > 255:
                print("Введите число, меньшее 256.")

            gpio.output(dac, dec_to_bin(n))

            print_volt(n)

finally:
    gpio.output(dac, 0)
    gpio.cleanup()
        
