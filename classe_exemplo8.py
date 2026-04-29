import os
os.system('cls')
from dataclasses import dataclass


@dataclass
class Funcionario:
    nome: str
    cpf: str
    matricula: int
    email: str
    setor: str
    telefone: int

@dataclass
class Cliente:
    nome: str
    email: str
    senha: int
    telefone: str

funcionario1 = Funcionario('João', '09272309506', 11017223, 'joao@gmail.com', 'Desenvolvedor', '71 98653-0183' )
cliente1 = Cliente('Maria', 'maria@gmail.com', '71 9865-0183', 29)

print(f'Nome: {cliente1.nome}')
print(f'E-mail: {cliente1.email}')
print(f'Numero de Telfone: {cliente1.senha}')
print(f'Data: {cliente1.telefone}')


print(f'Nome: {funcionario1.nome}')
print(f'CPF: {funcionario1.cpf}')
print(f'Matricula: {funcionario1.matricula}')
print(f'Email: {funcionario1.email}')
print(f'Setor: {funcionario1.setor}')
print(f'Telefone: {funcionario1.telefone}')