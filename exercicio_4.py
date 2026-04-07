import os
os.system('cls')

def inteiro():
    if valor >= 0:
        print(f'O valor {valor} é positivo')
    elif valor < 0:
        print(f'O valor {valor} é negativo')

valor = int(input('Insira o valor desejado: '))
inteiro()