# Função para calcular horas extras
def calcular_horas_extras(salario_base, horas):
    return salario_base * 0.015 * horas


# Função para calcular descontos por faltas
def calcular_descontos_faltas(salario_base, faltas):
    return salario_base * 0.02 * faltas


# Função para calcular bônus
def calcular_bonus(cargo, recebeu_bonus):
    if recebeu_bonus == "sim":
        if cargo == 1:
            return 1000
        elif cargo == 2:
            return 500
        elif cargo == 3:
            return 300
        elif cargo == 4:
            return 100
    return 0


# Entrada de dados
nome = input("Nome do funcionário: ")
cargo = int(input("Cargo (1-Gerente, 2-Analista, 3-Assistente, 4-Estagiário): "))
salario_base = float(input("Salário base: R$ "))
horas = int(input("Total de horas extras: "))
faltas = int(input("Total de faltas no mês: "))
recebeu_bonus = input("Recebeu bônus por desempenho? (sim/não): ").lower()


# Cálculos
horas_extras = calcular_horas_extras(salario_base, horas)
descontos = calcular_descontos_faltas(salario_base, faltas)
bonus = calcular_bonus(cargo, recebeu_bonus)

salario_bruto = salario_base + horas_extras + bonus
total_acrescimos = horas_extras + bonus
salario_final = salario_bruto - descontos


# Exibição dos resultados
print("\n--- Resumo salarial ---")
print(f"Funcionário: {nome}")
print(f"Salário bruto: R$ {salario_bruto:.2f}")
print(f"Total de acréscimos: R$ {total_acrescimos:.2f}")
print(f"Total de descontos: R$ {descontos:.2f}")
print(f"Salário final: R$ {salario_final:.2f}")