# Entrada de dados
estado = int(input("Digite o código do estado de origem (1 a 5): "))
peso = float(input("Digite o peso da carga em toneladas: "))
codigo_carga = int(input("Digite o código da carga (10 a 40): "))

# Conversão de toneladas para quilogramas
peso_kg = peso * 1000

# Inicialização da variável
preco = 0
imposto = 0

# Classificação de preço
if codigo_carga >= 10 and codigo_carga <= 20:
    preco = peso_kg * 100

elif codigo_carga >= 21 and codigo_carga <= 30:
    preco = peso_kg * 250

elif codigo_carga >= 31 and codigo_carga <= 40:
    preco = peso_kg * 340

# Calculando o valor dos impostos
if estado == 1:
    imposto = preco * 0.35

elif estado == 2:
    imposto = preco * 0.25

elif estado == 3:
    imposto = preco * 0.15

elif estado == 4:
    imposto = preco * 0.05

elif estado == 5:
    imposto = 0

# Calculando o total
preco_total = preco + imposto

# Exibindo os resultados e formatando
print(f"Preço da carga: R$ {preco:.2f}")
print(f"Imposto: R$ {imposto:.2f}")
print(f"Preço total: R$ {preco_total:.2f}")