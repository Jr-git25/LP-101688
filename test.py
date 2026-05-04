import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Cliente:
    nome: str
    idade: int
    peso: float
    altura: float
    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Peso: {self.peso}')
        print(f'Altura: {self.altura}')

lista_cliente =[]

print('Solicitando dados ')
for i in range(2):
    novo_cliente = Cliente(
        nome=input('Digite seu nome: '),
        idade=input('Digite sua idade: '),
        peso=input('Digite seu peso: '),
        altura=input('DIgite sua altura: ')
)
    lista_cliente.append(novo_cliente)
print('='*27)
print('Exibindo Dados do cliente')
print('='*27)
for cliente in lista_cliente:
    cliente.mostrar_dados()