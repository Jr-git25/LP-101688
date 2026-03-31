import os
os.system('cls')

pedidos = []
total = 0
novo_pedido = 'S'
while True:
    print('''
            Código          |           Prato           |           Valor
            1                        Picanha                     25,00
            2                        Lasanha                     20,00
            3                        Strogonoff                  18,00
            4                        Bifé Acebolado              15,00
            5                        Pão com ovo                 5,00        
    ''')

    codigo = int(input('Insira o codigo do pedido: '))

    match codigo:
        case codigo



    # if novo_pedido == 'S':
    #         print(pedidos)
    #         break
    # else:
    #         print('Atendimento encerrado')
