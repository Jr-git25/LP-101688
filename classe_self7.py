import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    telefone: str
    email: str


print('Solicitando dados do cliente.')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    telefone= input('Digite seu telefone: '),
    email= input('Digite seu email: ')
)

print("_ Exibindo dados do cliente _")
print(f"Nome: {cliente.nome}")
print(f"Telefone: {cliente.telefone}")
print(f"Email: {cliente.email}")
