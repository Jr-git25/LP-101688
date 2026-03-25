import os
os.system('cls')

vetor_notas = []
quantidade_notas = 3

print('Adicionando 3 notas.')
for i in range(quantidade_notas):
    nota = float(input(f'Digite a {i+1}ª nota: '))
#    Aciciona nota no vetor
    vetor_notas.append(nota)
# sum(vetor) = soma todas os valores no vetor
media = sum(vetor_notas) / quantidade_notas

print('\nExibindo as notas informadas.')
# ForEach = percorre o vetor sem informar a quantidade de elementos
# enumerate = atraves da variavel i, numera a quantidade de repetições
for uma_nota in vetor_notas:
    print(f'Nota: {uma_nota}')
print(f'Média: {media}')