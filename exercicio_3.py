import os
from dataclasses import dataclass

# # Configuração da Dataclass
# @dataclass
# class carro:
#     ano: str
#     marca: str
#     modelo: str
#     preco: float


@dataclass
class Modelo_carro:
    ano: int
    marca: str
    modelo: str
    
    def mostrar_dados_livro(self):
        print(f'Ano do carro: {self.ano}')
        print(f'Marca: {self.marca}')
        print(f'Modelo: {self.modelo}')
        print('-' * 20)

# --- Funções de Funcionalidade ---


NOME_DO_ARQUIVO = 'vista_carro.csv'

def cadastrar_carro():
    """Lê os dados do usuário e salva diretamente no arquivo CSV."""
    novo_carro = Modelo_carro(

        ano= int(input('Insira o ano do carro: ')),
        marca= input('Qual o marca do carro: '),
        modelo= input('Qual a modelo do carro: ')
        # print('✔ carro salvo com sucesso!')
    )
    with open(NOME_DO_ARQUIVO, 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{novo_carro.ano},{novo_carro.marca},{novo_carro.modelo}\n')

    return novo_carro

def listar_carros():
    """Lê o arquivo CSV e exibe os livros cadastrados."""
    print('\n= Consultar Catálogo =')
    
    if not os.path.exists(NOME_DO_ARQUIVO):
        print("O arquivo de catálogo ainda não existe. Cadastre um carro primeiro.")
        return

    lista_carros = []
    with open(NOME_DO_ARQUIVO, 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # strip() remove o \n e split(',') separa as colunas
            dados = linha.strip().split(',')
            if len(dados) == 4:
                ano, marca, modelo, preco = dados
                lista_carros.append(carro(ano, marca, modelo))

    if not lista_carros:
        print("Nenhum carro encontrado.")
    else:
        for carro in lista_carros:
            carro.mostrar_dados_livro()

def exibir_menu_carros():
    """Apenas imprime as opções do menu."""
    print("\n--- SISTEMA DE CADASTRO ---")
    print("1. Cadastrar Carros")
    print("2. Listar Carros")
    print("0. Sair")
    return input("Escolha uma opção: ")


def main():
    while True:
        opcao = exibir_menu_carros()

        match opcao:
            case 1:
                cadastrar_carro()
            case 2:
                listar_carros()
            case 0:
                print("Saindo do sistema... Até logo!")
                break
            case _:
                print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
