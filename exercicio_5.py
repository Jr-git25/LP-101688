import os
os.system('cls')

def calcular_media(n1, n2):
    media = (n1 + n2) / 2
    return media

def verificar_resultado(media):
    if media >= 7:
        resultado = 'Aprovado'
    else:
        resultado = 'Reprovado'
    return resultado


print('= Solicitando dados =')
n1 = int(input("Insira sua nota: "))
n2 = int(input("Insira sua nota: "))

media = calcular_media(n1, n2)
resultado = verificar_resultado(media)

print('\n Exibindo dados ')
print(f'Media {media}')
print(f'Resultado {resultado}')