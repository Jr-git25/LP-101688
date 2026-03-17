import os
os.system('cls')

soma = 0 


for i in range(3):
    nota = float(input(f''))
    soma = soma + nota
    media = soma / 3
if media >= 7:
     print(f'Aprovado: {media}')
elif media < 7:
        print('Recuperação')
elif media <= 4:
          print(f'Reprovado: {media}')
        
    







# n1 = int(input('Insira a primeira nota: '))
# n2 = int(input('Insira a segunda nota: '))
# n3 = int(input('Insira a terceira nota: '))
# n4 = int(input('Insira a quarta nota: '))

# media = n1 + n2 + n3 + n4 / 4

# if media > 7:
#     print(f"Aprovado: {media}")
# elif media < 4:
#     print(f'Reprovado: {media}')