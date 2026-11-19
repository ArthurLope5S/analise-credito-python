
# Sistema de Análise de Crédito
# Projeto desenvolvido em Python

# Validação do salário
salario = float(input("Digite o salário do cliente: R$ "))

while salario <= 0:
    print("Erro: O salário deve ser maior que zero.")
    salario = float(input("Digite um salário válido: R$ "))

# Validação do score
score = int(input("Digite o score do cliente (0 a 1000): "))

while score < 0 or score > 1000:
    print("Erro: O score deve estar entre 0 e 1000.")
    score = int(input("Digite um score válido: "))

# Análise de crédito
if score < 300:
    print("\n--- RESULTADO DA ANÁLISE ---")
    print("Empréstimo negado.")
    print("Motivo: Score insuficiente.")

else:
    if score <= 599:
        taxaJuros = 0.15
        taxaStr = "15%"
    elif score <= 849:
        taxaJuros = 0.10
        taxaStr = "10%"
    else:
        taxaJuros = 0.05
        taxaStr = "5%"

    # Cálculo do empréstimo
    valorEmprestimo = salario * 0.50
    jurosAnual = valorEmprestimo * taxaJuros
    valorTotal = valorEmprestimo + jurosAnual

    # Resultado
    print("\n--- RESULTADO DA ANÁLISE ---")
    print("Empréstimo aprovado!")
    print(f"Salário: R$ {salario:.2f}")
    print(f"Score: {score}")
    print(f"Taxa de juros anual: {taxaStr}")
    print(f"Valor do empréstimo: R$ {valorEmprestimo:.2f}")
    print(f"Juros anuais: R$ {jurosAnual:.2f}")
    print(f"Valor total: R$ {valorTotal:.2f}")
