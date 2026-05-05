import os
from dataclasses import dataclass

os.system("cls")
continuar = 's'

@dataclass
class Funcionario:
    nome: str
    cnpj: str
    telefone: str
    
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f': {self.cnpj}')



QUANTIDADE_FUNCIONARIOS = 2
lista_funcionario = []

print("_ Solicitando Dados _")


while True:
    novo_funcionario = Funcionario(
        nome=input('Digite seu nome: '),
        cnpj=input('Digite seu CNPJ: '),
        telefone=input('Digite seu numero de telefone: ')
    )
    print('Proximo Funcionario')
    lista_funcionario.append(novo_funcionario)

    continuar = input('Deseja continuar (S\N)? ')
    if continuar != 's':
        break

print('- Salvando Dados -')
with open('Contato_empresas.csv', 'a', encoding='utf-8') as arquivos:
    for funcionario in lista_funcionario:
        arquivos.write(f'Nome do Funcionario: {funcionario.nome}\n CNPJ do Funcionario: {funcionario.cnpj}\n Numero de telefone do funcionario: {funcionario.telefone}\n')
    print("Salvo com Sucesso!")

print('- Exibindo dados -')
for funcionario in lista_funcionario:
    funcionario.mostrar_dados()
print('='*25)
print('- Fim do Progama. -')
print('='*25)

# print('- Salvando Dados - ')
# with open('Lista de funcionarios.csv', 'a', encoding='utf-8') as arquivo:
#     for funcionario in lista_funcionario:
#         arquivo.write(f'{funcionario.nome}, {funcionario.idade}')
#     print('Salvo com sucesso!')

