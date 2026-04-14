import os
os.system('cls')
def nota_aritmetica(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media


media = 0
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

while nota1 < 0 or nota1 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota1 = float(input("Digite a primeira nota: "))    

while nota2 < 0 or nota2 > 10:
    print("Nota inválida! Digite uma nota entre 0 e 10.")
    nota2 = float(input("Digite a segunda nota: "))
media = nota_aritmetica(nota1, nota2)

if media >= 7:
    print("Aprovado!")
elif media >= 5:
    print("Reprovado!")
else:
    print("Recuperação!")
media = nota_aritmetica(nota1, nota2)
print(f"A média aritmética é: {media}")
