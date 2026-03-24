qnt_pares = 0
qnt_impares = 0
soma_pares = 0
soma_total = 0
total_numeros = 0

print("Digite números inteiros positivos (digite 0 para encerrar):")

while True:
    try:
        # Lê o número
        num = int(input("Digite um número: "))
        
        # Encerra a leitura
        if num == 0:
            break
            
        # Considera apenas positivos
        if num < 0:
            print("Por favor, digite apenas números positivos.")
            continue
            
        # Processamento
        total_numeros += 1
        soma_total += num
        
        if num % 2 == 0:
            qnt_pares += 1
            soma_pares += num
        else:
            qnt_impares += 1
            
    except ValueError:
        print("Entrada inválida. Digite um número inteiro.")

# Cálculo e exibição dos resultados
if total_numeros > 0:
    media_geral = soma_total / total_numeros
    media_pares = soma_pares / qnt_pares if qnt_pares > 0 else 0
    
    print("-" * 30)
    print(f"Quantidade de pares: {qnt_pares}")
    print(f"Quantidade de ímpares: {qnt_impares}")
    print(f"Média dos valores pares: {media_pares:.2f}")
    print(f"Média geral: {media_geral:.2f}")
else:
    print("Nenhum número positivo foi digitado.")