import os
os.system('cls')
from dataclasses import dataclass


@dataclass
class Funcionario:
    nome: str
    cpf: int
    matricula: int
    email: str
    setor: str

