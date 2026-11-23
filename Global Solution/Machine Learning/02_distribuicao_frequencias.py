import pandas as pd

dados = pd.read_csv("Dados tratados/FAANG_consolidado.csv")
# Variável discreta: Volume
# intervalos
freq_volume = pd.cut(dados['Volume'], bins=10)

# Frequência absoluta
freq_volume = freq_volume.value_counts().sort_index()

# Frequência relativa (%)
freq_relativa_volume = freq_volume / len(dados['Volume']) * 100

tabela_volume = pd.DataFrame({
    'Frequência Absoluta': freq_volume,
    'Frequência Relativa (%)': freq_relativa_volume
})

tabela_volume.index.name = None
print("\nTABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS - VOLUME")
print(f"\n{tabela_volume.round(2)}\n")

# Variável contínua: Preço de Fechamento
# intervalos
freq_preco = pd.cut(dados['Close'], bins=10)

# Frequência absoluta
freq_preco = freq_preco.value_counts().sort_index()

# Frequência relativa (%)
freq_relativa_preco = freq_preco / len(dados['Close']) * 100

tabela_preco = pd.DataFrame({
    'Frequência Absoluta': freq_preco,
    'Frequência Relativa (%)': freq_relativa_preco
})

tabela_preco.index.name = None
print("\nTABELA DE DISTRIBUIÇÃO DE FREQUÊNCIAS - PREÇO DE FECHAMENTO")
print(f"\n{tabela_preco.round(2)}\n")