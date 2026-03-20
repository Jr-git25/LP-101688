# Lista para armazenar as notas
notas = []

# Loop para coletar as 3 notas
for i in range(1, 4):
    while True:
        try:
            nota = float(input(f"Digite a {i}ª nota (0 a 10): "))
            
            # Validação do intervalo
            if 0 <= nota <= 10:
                notas.append(nota)
                break  # Sai do loop while e vai para a próxima nota
            else:
                print("Valor inválido! A nota deve estar entre 0 e 10.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

# Cálculo da média
media = sum(notas) / len(notas)

print("-" * 30)
print(f"Média Final: {media:.1f}")

# Verificação de status
if media >= 7:
    print("Status: APROVADO")
elif 5 <= media < 7:
    print("Status: RECUPERAÇÃO")
else:
    print("Status: REPROVADO")