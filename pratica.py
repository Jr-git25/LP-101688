from dataclasses import dataclass

@dataclass
class Funcionario:
    nome: str
    email: str
    telefone: str

    def mostrar_dados(self):
        print(f"Nome: {self.nome}")
        print(f"E-mail: {self.email}")
        print(f"Telefone: {self.telefone}")

lista_funcionario = []

continuar = 's'

while continuar == 's':
    print('===== Solicitando Dados do cliente =====')

    novo_funcionario = Funcionario(
        nome=input('Digite seu nome: '),
        email=input('Insira seu e-mail: '),
        telefone=input('Insira seu telefone: ')
    )

    lista_funcionario.append(novo_funcionario)

    continuar = input('Deseja continuar (S/N): ').lower()



print('='*25)
print('Exibindo dados do cliente')
print('='*25)

for funcionario in lista_funcionario:
    funcionario.mostrar_dados()