import pandas as pd

dados = pd.read_csv("Dados tratados/FAANG_consolidado.csv")

# ------------------------------------------------------------------
# FUNÇÕES DE TENDÊNCIA (implementadas manualmente, sem bibliotecas)
# ------------------------------------------------------------------

def calcular_media(valores):
    acumulador = 0

    for valor in valores:
        acumulador += valor

    media = acumulador / len(valores)
    return media

def calcular_mediana(valores):
    valores_ordenados = sorted(valores)
    quantidade = len(valores_ordenados)
    meio = quantidade // 2

    if quantidade % 2 == 0:
        mediana = (valores_ordenados[meio - 1] + valores_ordenados[meio]) / 2
    else:
        mediana = valores_ordenados[meio]

    return mediana

def calcular_moda(valores):
    frequencias = {}

    for valor in valores:
        if valor in frequencias:
            frequencias[valor] += 1
        else:
            frequencias[valor] = 1

    maior_frequencia = max(frequencias.values())

    if maior_frequencia == 1:
        return "Não há moda (nenhum valor se repete)"

    moda = []

    for valor, frequencia in frequencias.items():
        if frequencia == maior_frequencia:
            moda.append(valor)

    return moda

# ------------------------------------------------------------------
# FUNÇÕES DE DISPERSÃO (implementadas manualmente, sem bibliotecas)
# ------------------------------------------------------------------

def valor_maximo(valores):
    maior = valores.iloc[0]
    for num in valores:
        if num > maior:
            maior = num
    return maior
        
def valor_minimo(valores):
    menor = valores.iloc[0]
    for num in valores:
        if num < menor:
            menor = num
    return menor

def calcular_variancia(valores):
    media = calcular_media(valores)
    soma_quadrados = sum((valor - media) ** 2 for valor in valores)
    variancia = soma_quadrados / len(valores)
    return variancia

# EXIBIR OS DADOS
def mostrar_estatisticas(titulo, valores):
    media = calcular_media(valores)
    maximo = valor_maximo(valores)
    minimo = valor_minimo(valores)
    variancia = calcular_variancia(valores)
    quartis = valores.quantile([0.25, 0.50, 0.75])

    print(f"\n--- {titulo} ---")
    print(f"Média:         {calcular_media(valores):.2f}")
    print(f"Mediana:       {calcular_mediana(valores):.2f}")
    print(f"Moda:          {calcular_moda(valores)}")
    print(f"Máximo:        {maximo:.2f}")
    print(f"Mínimo:        {minimo:.2f}")
    print(f"Amplitude:     {maximo - minimo:.2f}")
    print(f"Variância:     {variancia:.2f}")
    print(f"Desvio padrão: {variancia ** 0.5:.2f}")
    print(f"Coeficiente de variação: {(variancia ** 0.5) / media * 100:.2f}%")
    print(f"Q1 (25%): {quartis[0.25]:.2f}")
    print(f"Q2 (50%): {quartis[0.50]:.2f}")
    print(f"Q3 (75%): {quartis[0.75]:.2f}")


# PROGRAMA PRINCIPAL
empresa_escolhida = input("Nome da empresa: ").strip().lower()
print("\n----------------------------ANÁLISE UNIVARIADA----------------------------")

grupo = dados[dados["Company"].str.lower() == empresa_escolhida]

if len(grupo) > 0:
    print(f"\nEmpresa: {empresa_escolhida.title()} | Registros: {len(grupo)}")

    mostrar_estatisticas("Preços de fechamento", grupo["Close"])
    mostrar_estatisticas("Volume", grupo["Volume"])
else:
    print("Empresa não encontrada!")