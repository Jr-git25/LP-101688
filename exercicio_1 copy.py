import os
from dataclasses import dataclass

os.system("cls")

@dataclass
class Funcionario:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Telefone: {self.telefone}')
        print(f'CNPJ: {self.cnpj}')

lista_funcionario = []

print("_ Solicitando Dados _")

while True:
    novo_funcionario = Funcionario(
        nome=input('Digite seu nome: '),
        cnpj=input('Digite seu CNPJ: '),  # melhor manter como string
        telefone=input('Digite seu numero de telefone: ')
    )

    lista_funcionario.append(novo_funcionario)

    continuar = input('Deseja continuar (S/N)? ').strip().lower()

    if continuar != 's':
        break

print('- Salvando Dados -')

with open('contato_empresas.csv', 'a', encoding='utf-8') as arquivos:
    for funcionario in lista_funcionario:
        arquivos.write(f'{funcionario.nome}, {funcionario.cnpj}, {funcionario.telefone}\n')

print("Salvo com Sucesso!")

print('- Exibindo dados -')
for funcionario in lista_funcionario:
    funcionario.mostrar_dados()
    print('-' * 20)

print('='*25)
print('- Fim do Programa -')
print('='*25)