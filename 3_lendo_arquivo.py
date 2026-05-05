import os
from dataclasses import dataclass

os.system('cls')
@dataclass
class Empresa:
    nome: str
    cnpj: str
    telefone: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'CNPJ: {self.cnpj}')
        print(f'Telefone: {self.telefone}\n')


lista_empresa = []

with open('contato_empresas.csv', 'r') as arquivos:
    for linha in arquivos:
        nome, cnpj, telefone = linha.strip().split(',')
        lista_empresa.append(Empresa(nome=nome, cnpj=cnpj, telefone=telefone))

for empresa in lista_empresa:
    empresa.mostrar_dados()