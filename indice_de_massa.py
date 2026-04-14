import os
os.system('cls') 
def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc  
peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altura em metros: "))
imc = calcular_imc(peso, altura)
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



