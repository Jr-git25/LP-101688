import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float
    def mostrar_dados(self):
        print(f"Seu nome e: {self.nome}")
        print(f"Sua idade e: {self.idade}")
        print(f"Seu peso e: {self.peso}")
        print(f"Sua altura e: {self.altura}")
paciente1 = Paciente(
    nome= input('Insira seu nome: '),
    idade= input('Insira sua idade: '),
    peso= input('Insira seu peso KG: '),
    altura= input('Insira sua altura: '),
)
print('\n Exibir dados do cliente')

paciente1.mostrar_dados()
