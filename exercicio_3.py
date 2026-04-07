import os
os.system('cls')

def numero():
    for i in range(1):
        numero = float(input('Insira o numero desejado: '))
    if numero % 2 == 0:
        print("Este numero e par")
    else:
        print('Este numero e impar')
numero()