import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Endereco:
    logradouro: str
    numero: int

@dataclass
class Cliente:
    nome: str
    idade: int
    endereco: Endereco

    def mostrar_dados(self):
        print("_ Exibindo dados do cliente _")
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")
        print(f"Endereço: {self.endereco.logradouro}")
        print(f'Numero: {self.endereco.logradouro}')



print('Solicitando dados do cliente.')
cliente = Cliente(
    nome= input('Digite seu nome: '),
    idade= input('Digite sua idade: '),
    endereco= Endereco(
        logradouro= input("Digite seu endereco: "),
        numero= input('Digite o numero: ')
    )
)
print('='*27)
print('\n Exibindo dados do cliente')
print('='*27)
cliente.mostrar_dados()
