vetor = []

for i in range(5):
    numero = float(input(f"Digite o {i+1}º número: "))
    
    if numero < 0:
        vetor.append(0)
    else:
        vetor.append(numero)


print("\nValores armazenados no vetor (negativos substituídos por 0):")
print(vetor)

