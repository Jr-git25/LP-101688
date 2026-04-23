import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

# --- CONSTANTES DE ALÍQUOTAS ---
DESC_INSS = {
    "FAIXA1": 0.075,
    "FAIXA2": 0.09,
    "FAIXA3": 0.12,
    "FAIXA4": 0.14
}

DESC_IRRF = {
    "FAIXA1": 0.075,
    "FAIXA2": 0.15,
    "FAIXA3": 0.225,
    "FAIXA4": 0.275
}

print('-' * 20)
print('SISTEMA DE FOLHA')
print('-' * 20)

# 1- Cadastro
def obter_dados():
    matricula = input('Insira sua matricula: ')
    senha = input('Insira sua senha: ')
    return matricula

# 2- Salário
def obter_salario():
    while True:
        try:
            return float(input('Insira seu salário base em R$: '))
        except ValueError:
            print("Por favor, digite um valor numérico válido.")

# Execução das funções de entrada
matricula_usuario = obter_dados()
salario_base = obter_salario()

# 3- Vale transporte
vale_transporte = input('\nDeseja receber vale transporte (s/n): ').lower()
if vale_transporte == 's':
    print('Vale transporte solicitado (Desconto de 6% sobre o base).')
    valor_vt = salario_base * 0.06
else:
    print('Vale transporte não solicitado.')
    valor_vt = 0

# 4- Vale Alimentação e Dependentes
vale_alimentacao = float(input('Quanto a empresa fornece de vale alimentação? R$ '))
dependentes = int(input('Quantos dependentes você possui? '))

# --- CÁLCULO INSS ---
print('\n--- Tabela INSS Aplicada ---')
if salario_base <= 1518.00:
    aliquota_inss = DESC_INSS["FAIXA1"]
    msg_inss = "7.5%"
elif salario_base <= 2793.88:
    aliquota_inss = DESC_INSS["FAIXA2"]
    msg_inss = "9%"
elif salario_base <= 4190.83:
    aliquota_inss = DESC_INSS["FAIXA3"]
    msg_inss = "12%"
elif salario_base <= 8157.41:
    aliquota_inss = DESC_INSS["FAIXA4"]
    msg_inss = "14%"
else:
    aliquota_inss = 0 # Teto do INSS (simplificado)
    msg_inss = "Teto (R$ 951,62)"

valor_inss = salario_base * aliquota_inss if aliquota_inss > 0 else 951.62
print(f'Desconto INSS: {msg_inss} -> R$ {valor_inss:.2f}')

# --- CÁLCULO IRRF (Baseado na sua tabela) ---
# Base de cálculo do IRRF é o salário menos o INSS
base_irrf = salario_base - valor_inss

print('\n--- Tabela IRRF Aplicada ---')
if base_irrf <= 2428.80:
    valor_irrf = base_irrf * DESC_IRRF["FAIXA1"]
    msg_irrf = "7.5%"
elif base_irrf <= 2826.65:
    valor_irrf = 0
    msg_irrf = "Isento"
elif base_irrf <= 3751.05:
    valor_irrf = base_irrf * DESC_IRRF["FAIXA3"]
    msg_irrf = "22.5%"
elif base_irrf <= 4664.68:
    valor_irrf = base_irrf * DESC_IRRF["FAIXA4"]
    msg_irrf = "27.5%"
else:
    valor_irrf = base_irrf * 0.275 # Mantendo o teto da sua tabela
    msg_irrf = "27.5% (Acima do teto)"

print(f'Desconto IRRF: {msg_irrf} -> R$ {valor_irrf:.2f}')

# --- RESUMO FINAL ---
salario_liquido = salario_base - valor_inss - valor_irrf - valor_vt + vale_alimentacao

print('\n' + '='*30)
print(f'RESUMO PARA MATRÍCULA: {matricula_usuario}')
print(f'Salário Base: R$ {salario_base:.2f}')
print(f'Total Descontos: R$ {(valor_inss + valor_irrf + valor_vt):.2f}')
print(f'Benefícios (VA): R$ {vale_alimentacao:.2f}')
print(f'SALÁRIO LÍQUIDO: R$ {salario_liquido:.2f}')
print('='*30)