# Vetores com dados dos exames
codigos = [1, 2, 3, 4, 5, 6, 7]
nomes = [
    "Hemograma",
    "Raio-X",
    "Tomografia",
    "Ressonância",
    "Ultrassom",
    "Eletrocardiograma",
    "Exame de Sangue"
]
precos = [50.0, 80.0, 200.0, 350.0, 120.0, 90.0, 60.0]

# Listas para armazenar exames escolhidos
escolhidos_codigos = []
escolhidos_nomes = []
subtotal = 0

while True:
    print("\n--- LISTA DE EXAMES ---")
    for i in range(len(codigos)):
        print(f"Código: {codigos[i]} | Nome: {nomes[i]} | Preço: R${precos[i]:.2f}")
    print("Digite 0 para finalizar")

    codigo = int(input("Digite o código do exame: "))

    if codigo == 0:
        break

    if codigo not in codigos:
        print("Código inválido! Tente novamente.")
        continue

    indice = codigos.index(codigo)

    escolhidos_codigos.append(codigo)
    escolhidos_nomes.append(nomes[indice])
    subtotal += precos[indice]

    continuar = input("Deseja agendar outro exame? (s/n): ").lower()
    if continuar != 's':
        break

# Forma de pagamento
print("\nFormas de pagamento:")
print("1 - Convênio (15% desconto)")
print("2 - Particular (sem desconto)")
print("3 - Cartão de crédito (8% acréscimo)")

opcao = int(input("Escolha a forma de pagamento: "))

desconto = 0
acrescimo = 0

if opcao == 1:
    desconto = subtotal * 0.15
    total = subtotal - desconto
    forma = "Convênio"
elif opcao == 2:
    total = subtotal
    forma = "Particular"
elif opcao == 3:
    acrescimo = subtotal * 0.08
    total = subtotal + acrescimo
    forma = "Cartão de crédito"
else:
    print("Opção inválida! Considerando pagamento Particular.")
    total = subtotal
    forma = "Particular"

# Exibir resultados
print("\n--- RESULTADO ---")
print("Exames escolhidos:")
for i in range(len(escolhidos_codigos)):
    print(f"Código: {escolhidos_codigos[i]} | Nome: {escolhidos_nomes[i]}")

print(f"\nSubtotal: R${subtotal:.2f}")
print(f"Forma de pagamento: {forma}")

if desconto > 0:
    print(f"Desconto aplicado: R${desconto:.2f}")
elif acrescimo > 0:
    print(f"Acréscimo aplicado: R${acrescimo:.2f}")
else:
    print("Sem desconto ou acréscimo")

print(f"Valor final: R${total:.2f}")
