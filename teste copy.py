import os

# Função sem retorno.=

# Definindo listas vazias para armazenar os dados dos usuários
nomes = []
alturas = []
pesos = []
imcs = []

def calcular_imc(peso, altura):
    imc = peso / (altura ** 2)
    return imc  


def averiguar_condicao(imc):
    if imc < 18.5:
        classificacao = print('Abaixo do peso')
        recomendacao = print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
    elif imc >= 18.5:
        classificacao = print('Peso normal')
        recomendacao = print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
    elif imc >= 25:
        classificacao = print('Sobrepeso')
        recomendacao = print('Continue mantendo um estilo de vida saudável, com alimentação equilibrada e prática regular de exercícios físicos.')
    elif imc >= 30:
        classificacao = print('Obesidade Grau I')
        recomendacao = print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
    elif imc >= 35:
        classificacao = print('Obesidade Grau II')
        recomendacao = print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
    elif imc >= 40:
        classificacao = print('Obesidade Grau III')
        recomendacao = print('Recomenda-se consultar um profissional de saúde para avaliação e orientação adequada.')
    return classificacao, recomendacao

while True:
    
    nome = input('Digite o seu nome completo: ')
    altura = float(input('Digite a sua altura: '))
    peso = float(input('Digite o seu peso: '))

    nomes.append(nome)
    alturas.append(altura)
    pesos.append(peso)
    imcs.append(imc)

    imc = calcular_imc(peso, altura)

    classificacao, recomendacao = averiguar_condicao(imc)

    print('\n= Exibindo dados =')
    print(f'Nome: {nome}')
    print(f'Altura: {altura}')
    print(f'Peso: {peso}')
    print(f"Seu IMC é: {imc:.2f}")
    print(f'Classificação: {classificacao}')
    print(f'Recomendação: {recomendacao}')

    continuar = input('Deseja continuar (s/n): ')
    if continuar != 's':
        print('Programa encerrado')
        break

print(' ====  Todos os usuarios ==== ')
for i in range(len(nomes)):
    print(f'Nome: {nomes[i]} - IMC: {imcs[i]:.2f}')
