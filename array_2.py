vetor = []
soma_positivos = 0
qtd_negativos = 0

print("Digite 5 números:")
for i in range(5):
    num = float(input(f"Número {i+1}: "))
    vetor.append(num)
    
    if num > 0:
        soma_positivos += num
    elif num < 0:
        qtd_negativos += 1

print("-" * 30)
print(f"Vetor: {vetor}")
print(f"Quantidade de números negativos: {qtd_negativos}")
print(f"Soma dos números positivos: {soma_positivos}")














# import os
# os.system('cls')

# negativos = []
# soma_positivos = []

# for i in range(5):
#     num = int(input("Insira o numero desejado:  "))
# if num >= 0:
#     soma_positivos.append(num)
# else:
#     negativos.append(num)
# print(f'Quantidade numero negativos: {negativos}')
# print(f'Soma numeros positivos:  'sum(soma_positivos))