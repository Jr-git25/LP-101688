

import os
os.system('cls')

def calcular_ano_nascimento(idade, ano_atual):
    return ano_atual - idade

idade = int(input("Digite sua idade: "))
ano_atual = int(input("Digite o ano atual: "))
ano_nascimento = calcular_ano_nascimento(idade, ano_atual)

print(f"Você nasceu no ano de: {ano_nascimento}")
print("Obrigado por usar o programa!")