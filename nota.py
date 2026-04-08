import os
os.system('cls')

notas = []
quantidade_notas = 3
for i in range(quantidade_notas):
    nota = int(input('Insira sua nota: '))
    notas.append(nota)
media = nota / 3
media_final = media
print(f'Sua media foi: {media}')
def total():
    print(f'Sua media final foi {media_final}')