import os

def convert_value(input):
    try:
        return float(input)
    except:
        print('Entrada invalida')
        return -1

def clear():
    os.system('clear')