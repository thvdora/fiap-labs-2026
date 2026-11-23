anos = int(input("Digite sua idade em anos: "))
meses = int(input("Digite sua idade em meses: "))
dias = int(input("Digite sua idade em dias: "))

# Conversões
anos_em_dias = anos * 365
meses_em_dias = meses * 30
total_dias = anos_em_dias + meses_em_dias + dias

print(f"Sua idade em dias é: {total_dias}")