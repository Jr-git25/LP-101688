
import os

os.system("cls")
numeros = []
pares = []
impares = []
maior = []
menor = []
negativos = 0
positivo = 0

# Variáveis para armazenar os números
for i in range(5):
    num = int(input('Insira o valor do num: '))
    numeros.append(num)
# Variáveis para armazenar as estatísticas

def numeros_pares():
    if num % 2 == 0:
        pares.append(num)
    else:
   impares
    if num < 0:
        quantidade_positivos += 1
    elif num < 0:
        quantidade_negativos += 1
quantidade_pares = 0
quantidade_impares = 0
soma_impares = 0
soma_geral = 0
soma_pares = 0
quantidade_positivos = 0
maior_numero = 0    
menor_numero = 0
quantidade_negativos = 0
# Processando cada número
# if num % 2 == 0:
#     quantidade_pares += 1
#     soma_pares += num
# else:
#     quantidade_impares = 1
#     soma_impares += num

# if num < 0:
#     quantidade_positivos += 1


# Processando o segundo número
# if num % 2 == 0:
#     quantidade_pares += 1
#     soma_pares += num
# else:
#     quantidade_impares += 1
#     soma_impares += num

# if num > 0:
#     quantidade_positivos += 1
# elif num < 0:
#     quantidade_negativos += 1
total_inseridos = len(numeros)
maior_numero = max(numeros)
menor_numero = min(numeros)
media_total = sum(numeros) / total_inseridos

media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0
media_impares = sum(impares) / len(impares) if len(impares) > 0 else 0

# Calculando as médias


# Imprimindo as estatísticas
print('\n' + '='*30)
print('     RELATORIO FINAL')
print('='*30)
print(f'Pares: {len(pares)} | impares: {len(impares)}')
print(f'Positivos: {positivo} | negativo: {impares}')
print(f'Total de num inseridos: {total_inseridos}')
print(f'Maior numero: {maior_numero} | menor Numero: {menor_numero}')
print(f'Media dos pares: {media_pares:.3f}')
print(f'Media dos impares: {media_impares:.3f}')
print(f'Media geral: {media_total:.3f}')



print(f'Numeros na ordem inversa: {numeros[::-1]}')
print('='*30)










# print("\nEstatísticas dos números:")
# print(f"Quantidade de pares: {quantidade_pares}")
# print(f"Quantidade de ímpares: {quantidade_impares}")
# print(f"Quantidade de positivos: {quantidade_positivos}")
# print(f"Quantidade de negativos: {quantidade_negativos}")
# print(f'Maior num: {maior_numero}')
# print(f'Menor num: {menor_numero}')