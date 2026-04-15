import os
os.system('cls')

# Inicialização das variáveis e listas
numeros = []
pares = []
impares = []
positivos = 0
negativos = 0

# Leitura de 5 números inteiros
for i in range(5):
    num = int(input(f"Digite o {i+1}º número inteiro: "))
    numeros.append(num)
    
    # Verificação de par ou ímpar
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
        
    # Verificação de positivo ou negativo
    if num > 0:
        positivos += 1
    elif num < 0:
        negativos += 1

# Processamento de estatísticas
total_inseridos = len(numeros)
maior_num = max(numeros)
menor_num = min(numeros)
media_total = sum(numeros) / total_inseridos

# Médias condicionais (prevenção de erro de divisão por zero)
media_pares = sum(pares) / len(pares) if len(pares) > 0 else 0
media_impares = sum(impares) / len(impares) if len(impares) > 0 else 0

# Exibição dos resultados
print("\n" + "="*30)
print("       RELATÓRIO FINAL")
print("="*30)
print(f"Pares: {len(pares)} | Ímpares: {len(impares)}")
print(f"Positivos: {positivos} | Negativos: {negativos}")
print(f"Total de números inseridos: {total_inseridos}")
print(f"Maior número: {maior_num} | Menor número: {menor_num}")
print(f"Média dos pares: {media_pares:.2f}")
print(f"Média dos ímpares: {media_impares:.2f}")
print(f"Média geral: {media_total:.2f}")

# Exibição na ordem inversa
# O comando [::-1] cria uma cópia da lista de trás para frente
print(f"Números na ordem inversa: {numeros[::-1]}")
print("="*30)