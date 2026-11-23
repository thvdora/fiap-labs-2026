reais = float(input("Digite um valor em reais: R$ "));

# Fazendo as conversões com os valores dados
dolar = reais / 4.99
euro = reais / 5.59
peso_argentino = reais / 0.0034
libra = reais / 6.59
iene = reais / 0.32

print("\n--- CONVERSÃO ---")
print(f"Dólar Americano: US$ {dolar:.2f}")
print(f"Euro: € {euro:.2f}")
print(f"Peso Argentino: AR$ {peso_argentino:.2f}")
print(f"Libra Esterlina: £ {libra:.2f}")
print(f"Iene: ¥ {iene:.2f}")