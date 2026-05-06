import os
from dataclasses import dataclass

# Configuração da Dataclass
@dataclass
class Livro:
    nome: str
    autor: str
    categoria: str
    preco: float

    def mostrar_dados_livro(self):
        print(f'Nome: {self.nome}')
        print(f'Autor: {self.autor}')
        print(f'Categoria: {self.categoria}')
        print(f'Valor: R$ {self.preco}')
        print('-' * 20)

# --- Funções de Funcionalidade ---

def cadastrar_livros():
    """Lê os dados do usuário e salva diretamente no arquivo CSV."""
    print('\n= Cadastro de Livro =')
    nome = input('Insira o nome do carro: ')
    autor = input('Qual o : ')
    categoria = input('Qual a categoria do livro: ')
    
    try:
        preco = float(input('Qual o valor do livro: '))
    except ValueError:
        print("Preço inválido! Usando 0.0")
        preco = 0.0

    # Salvando no arquivo (modo 'a' para append/anexar)
    with open('Catalogo_livros.csv', 'a', encoding='utf-8') as arquivo:
        arquivo.write(f'{nome},{autor},{categoria},{preco}\n')
    
    print('✔ Livro salvo com sucesso!')

def listar_livros():
    """Lê o arquivo CSV e exibe os livros cadastrados."""
    print('\n= Consultar Catálogo =')
    
    if not os.path.exists('Catalogo_livros.csv'):
        print("O arquivo de catálogo ainda não existe. Cadastre um livro primeiro.")
        return

    lista_livro1 = []
    with open('Catalogo_livros.csv', 'r', encoding='utf-8') as arquivo:
        for linha in arquivo:
            # strip() remove o \n e split(',') separa as colunas
            dados = linha.strip().split(',')
            if len(dados) == 4:
                nome, autor, categoria, preco = dados
                lista_livro1.append(Livro(nome, autor, categoria, float(preco)))

    if not lista_livro1:
        print("Nenhum livro encontrado.")
    else:
        for livro in lista_livro1:
            livro.mostrar_dados_livro()

def exibir_menu_carros():
    """Apenas imprime as opções do menu."""
    print("\n--- SISTEMA DE CADASTRO ---")
    print("1. Cadastrar Carros")
    print("2. Listar Carros")
    print("0. Sair")
    return input("Escolha uma opção: ")

# --- Fluxo Principal ---

def main():
    while True:
        opcao = exibir_menu_carros()

        match opcao:
            case "1":
                cadastrar_livros()
            case "2":
                listar_livros()
            case "0":
                print("Saindo do sistema... Até logo!")
                break
            case _:
                print(" Opção inválida! Tente novamente.")

if __name__ == "__main__":
    main()
    