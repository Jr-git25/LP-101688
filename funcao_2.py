import os
os.system('cls')
# Função com parâmetros
def somar(n1, n2):
    for i in range(1, 11):
        print(f'Numereo atual {i}')
        soma = n1 + n2
        print(f'Soma: {soma}')

primeiro_numero = int(input('Digite o primeiro numero: '))
segundo_numero = int(input('Digite o segundo numero: '))

somar(primeiro_numero, segundo_numero)