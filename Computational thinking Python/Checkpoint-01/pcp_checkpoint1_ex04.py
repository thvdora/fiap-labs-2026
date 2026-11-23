idade_em_dias = int(input("Digite sua idade em dias: "))
idade_em_anos = idade_em_dias // 365
idade_em_meses = (idade_em_dias % 365) // 30
idade_em_dias_restantes = (idade_em_dias % 365) % 30

print(f"Sua idade é: {idade_em_anos} anos, {idade_em_meses} meses e {idade_em_dias_restantes} dias")