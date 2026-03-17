import os
os.system('cls')


pares = 0
impares = 0

for i in range(5):
    numero = int(input(f'Digite o {i+1} numero: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
print(f'Quantidade de numeros impares: {impares}, \n Quantidade de numeros pares: {pares}')







# n1 = int(input('Insira o valor desejado: '))
# n2 = int(input('Insira o valor desejado: '))
# n3 = int(input('Insira o valor desejado: '))
# n4 = int(input('Insira o valor desejado: '))
# n5 = int(input('Insira o valor desejado: '))

# for i in range(1, 11):
    