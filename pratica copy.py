import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: float
    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

lista_funcionario = []
while True:
    print('===== Solicitando Dados do cliente =====')
    novo_funcionario = Funcionario(
            nome=input('Digite seu nome: '),
            email=input('Insira seu e-mail: '),
            telefone=input('Insira seu telefone: ')
        )
    continuar = input('Deseja continuar (S\N): ').lower()
    lista_funcionario.append(novo_funcionario)
    
    
    if continuar != 's':
        print('Prosseguindo com atendimento...')
        break

print('='*25)
print('Exibindo dados do cliente')
print('='*25)
for funcionario in lista_funcionario:
    funcionario.mostrar_dados()