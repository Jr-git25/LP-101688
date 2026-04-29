import os
os.system('cls')
from dataclasses import dataclass

@dataclass
class Paciente:
    nome: str
    idade: int
    peso: float
    altura: float

paciente1 = Paciente(
    nome= input('Insira seu nome: '),
    idade= input('Insira sua idade: '),
    peso= input('Insira seu peso KG: '),
    altura= input('Insira sua altura: '),
)
print('Mostrando dados')

print(f"Seu nome e: {paciente1.nome}")
print(f"Sua idade e: {paciente1.idade}")
print(f"Seu peso e: {paciente1.peso}")
print(f"Sua altura e: {paciente1.altura}")