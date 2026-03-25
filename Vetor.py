import os
os.system('cls')

# notas = []
# quantidade_notas = 4

# print('Adicionando 4 notas.')
# for i in range(quantidade_notas):
#     nota = float(input(f'Digite a {i+1}ª nota: '))
# #    Aciona nota no vetor
#     notas.append(nota)
# # sum(vetor) = soma todas os valores no vetor
# media = sum(notas) / quantidade_notas



# if media >= 7:
#     resultado = 'Aprovado'
# elif media >= 5:
#     resultado = 'Recuperação'
# else:
#     resultado = 'Reprovado'

# print('\nExibindo as notas informadas.')
# # ForEach = percorre o vetor sem informar a quantidade de elementos
# # enumerate = atraves da variavel i, numera a quantidade de repetições
# for uma_nota in notas:
#     print(f'Nota: {uma_nota}')
# print(f'Média: {media}')
# print(f'Resultado: {resultado}')


num = []
quantidade_numeros = 6
pares = 0
impares = 0

for i in range(quantidade_numeros):
    numero = float(input(f'Digite o {i+1}º número: '))
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

# Exibindo os resultados
print(f'Quantidade de números pares: {pares}')
print(f'Quantidade de números ímpares: {impares}')


# maior_numero = max(num)
# menor_numero = min(num)

# print('\nExibindo os números informados.')
# print(f'Maior número: {maior_numero}')
# print(f'Menor número: {menor_numero}')
