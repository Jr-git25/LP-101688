import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Fornecedor:
    nome: str
    email: str
    telefone: str
    endereco: str

fornecedor1 = Fornecedor(
    nome= input('Insira seu nome: '),
    email= input("Insira seu email: "),
    telefone= input('Insira seu numero de telfone: '),
    endereco= input('Insira seu endereço: '),
    )

print(f"Seu nome e: {fornecedor1.nome}")
print(f"Seu email e: {fornecedor1.email}")
print(f"Seu telefone e: {fornecedor1.telefone}")
print(f"Seu endereço e: {fornecedor1.endereco}")