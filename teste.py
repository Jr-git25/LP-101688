import os

# Função sem retorno.
def logoSenai():
    os.system("cls || clear")
    print("=== SENAI === ")

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
idades = []
alturas = []
pesos = []

# Solicitando os dados dos usuários em um loop
while True:
    logoSenai()
    nome = input("Digite o nome do usuário (ou digite 'sair' para encerrar): ")
    
    
    # Verificando se o usuário quer sair
    if nome.lower() == 'sair':
        break
    
    idade = int(input("Digite a idade do usuário: "))
    altura = float(input("Digite a altura do usuário (em metros): "))
    peso = float(input("Digite o peso do usuário (em quilogramas): "))
    
    # Adicionando os dados às listas
    nomes.append(nome)
    idades.append(idade)
    alturas.append(altura)
    pesos.append(peso)

def imc_final(peso, altura):
    imc = peso / (altura ** 2)
    return imc  
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = imc_final(peso, altura)
print(f"Seu IMC é: {imc:.2f}")
if imc < 18.5:
    print('Abaixo do peso')
    print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
elif imc < 25:
    print('Peso normal')
    print('Continue mantendo um estilo de vida saudável, com alimentação equilibrada e prática regular de exercícios físicos.')
elif imc < 30:
    print('Sobrepeso')
    print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
elif imc < 35:
    print('Obesidade Grau I')
    print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
elif imc < 40:
    print('Obesidade Grau II')
    print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
else:
    print('Obesidade Grau III')
    print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
print("Obrigado por usar o programa!")
    
calcular_imc = imc_final(peso, altura)
# Exibindo os dados armazenados
logoSenai()
print("\nDados dos usuários:")
for i in range(len(nomes)):
    print(f"Usuário {i+1}:")
    print("Nome:", nomes[i])
    print("Idade:", idades[i])
    print("Altura:", alturas[i], "metros")
    print("Peso:", pesos[i], "quilogramas")
    print('Seu imc foi:', imc)
    print()