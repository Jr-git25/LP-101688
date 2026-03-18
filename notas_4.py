import os
os.system('cls')

soma = 0
quantidade_notas = 3

for i in range(quantidade_notas):
    while True:
        nota = float(input(f'Insira a nota: '))
        if nota >= 0 and nota <= 10:
            soma += nota
            break
        else:
            print('Nota invalida! Insira a nota de 0 a 10')

media = soma / quantidade_notas

print(f'\n Media final: {media}')

if media >= 7:
    print('Aprovado!')
elif media >= 5:
    print('Recuperação')
else:
    print("Reprovado")





















# n1 = int(input('Insira a primeira nota: '))
# n2 = int(input('Insira a primeira nota: '))
# n3 = int(input('Insira a primeira nota: '))


# media = n1 + n2 + n3 / 3

# notas = 3

# for i in range(notas):




