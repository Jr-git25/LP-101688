import os
os.system('cls')

from dataclasses import dataclass


@dataclass
class Pessoa:
    nome: str
    idade: int


@dataclass
class Pet:
    nome: str
    idade: int

pessoa1 = Pessoa('Alice', 20)
pessoa2 = Pessoa('Bob', 30)

pet1 = Pet('Borabill', 4)
pet2 = Pet('Tusk', 2)

print(f'Nome: {pessoa1.nome} \n Idade: {pessoa1.idade}')
print(f'Nome: {pessoa2.nome} \n idade: {pessoa2.idade}')
print(f'Nome: {pet1.nome} \n Idade: {pet1.idade}')
print(f'Nome: {pet2.nome} \n idade: {pet2.idade}')