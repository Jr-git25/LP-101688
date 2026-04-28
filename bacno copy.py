import os
os.system('cls')

def criar_usuario():
    nome = input('Digite o nome do usuario: ')
    senha = int(input('Insira sua senha de cadastro: '))
    print(f"Usuario {nome} criado com sucesso!")

def sacar(saldo):
    valor = float(input('Digite o valor para saque: R$ '))
    if valor > saldo:
        print('Saldo insuficiente!')
    elif valor <= 0:
        print('Valor invalido!')
    else:
        saldo -= valor
        print(f'Saque de R${valor} realizado!')
    return saldo

def depositar(saldo):
    valor = float(input('Digite o valor para deposito: R$ '))
    if valor <= 0:
        print('Valor invalido')
    else:
        saldo += valor
        print(f'Deposito de R${valor} realizado!')
    return saldo

def ver_saldo(saldo):
    print(f'Seu saldo atual é: R$ {saldo:.2f}')

def menu():
    saldo = 0.0

    while True:
        print('\n=== BANCO JL DIGITAL ===')
        print('1- Criar o usuario')
        print('2- Sacar')
        print('3- Depositar')
        print('4- Saldo')
        print('5- Sair')
        opcao = input('Escolha uma opção: ')

        if opcao == '1':
            criar_usuario()
        elif opcao == '2':
            saldo = sacar(saldo)
        elif opcao == '3':
            saldo = depositar(saldo)
        elif opcao == '4':
            ver_saldo(saldo)
        elif opcao == '5':
            print('Saindo...')
            break
        else:
            print('Opção invalida!')

menu()