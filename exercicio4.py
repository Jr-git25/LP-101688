import os
os.system('cls' if os.name == 'nt' else 'clear')

from dataclasses import dataclass

@dataclass
class Pet:
    nome: str
    idade: int
    raca: str

    def mostrar_dados(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Raça: {self.raca}')
        print('-' * 20)

lista_do_pet = []

continuar = 's'

while continuar == 's':
    print('===== Solicitando Dados do Pet =====')

    nome = input('Insira o nome do seu Pet: ')
    
    
    while True:
        try:
            idade = int(input('Insira a idade do seu Pet: '))
            break
        except ValueError:
            print('Digite uma idade válida (número inteiro).')

    raca = input('Insira a raça do seu Pet: ')

    novo_pet = Pet(nome=nome, idade=idade, raca=raca)
    lista_do_pet.append(novo_pet)

    continuar = input('Deseja prosseguir (S/N): ').lower()

print('\n' + '='*23)
print('Exibindo dados dos Pets')
print('='*23)

for pet in lista_do_pet:
    pet.mostrar_dados()