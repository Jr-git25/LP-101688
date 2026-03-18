import os
os.system('cls')

while True:
    usuario = input('Insira seu usuario: ')
    password = input('Insira sua senha: ')
    senha = '1234'
    login = 'Lucas'

    if usuario == login and password == senha:
        print('Acesso liberado')
        break
    else:
        print('Acesso negado')
        
