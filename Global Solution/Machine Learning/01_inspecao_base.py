import pandas as pd

## CARREGANDO E CONHECENDO TODAS AS BASES DE DADOS
amazon = pd.read_csv("Dados originais/Amazon.csv")
apple = pd.read_csv("Dados originais/Apple.csv")
facebook = pd.read_csv("Dados originais/Facebook.csv")
google = pd.read_csv("Dados originais/Google.csv")
netflix = pd.read_csv("Dados originais/Netflix.csv")

# FUNÇÃO PARA CONHECER CADA BASE DE DADOS
def inspecionar_base_dados(df, nome_base):
    print(f"\n----------------------------BASE DE DADOS {nome_base.upper()}----------------------------")
    print("\nDIMENSÕES DA BASE - linhas x colunas:")
    print(df.shape)
    print("\nCOLUNAS:")
    print(df.columns)
    print("\nTIPOS DE DADOS:")
    print(df.dtypes)
    print("\nVALORES AUSENTES:")
    print(df.isnull().sum())
    print("\nPRIMEIROS REGISTROS:")
    print(df.head())
    print("\n-----------------------------------------------------------------------------\n")

inspecionar_base_dados(amazon, "Amazon")
inspecionar_base_dados(apple, "Apple")
inspecionar_base_dados(facebook, "Facebook")
inspecionar_base_dados(google, "Google")
inspecionar_base_dados(netflix, "Netflix")

# Verificando onde estão os dados ausentes e removendo-os
print(apple[apple.isnull().any(axis=1)])
apple = apple.dropna()
print(apple.isnull().sum())
print(apple.shape)

# Criando uma nova coluna para distinguir as empresas
amazon["Company"] = "Amazon"
apple["Company"] = "Apple"
facebook["Company"] = "Facebook"
google["Company"] = "Google"
netflix["Company"] = "Netflix"

# Unificando as empresas em uma única tabela
dados = pd.concat([amazon, apple, facebook, google, netflix], ignore_index=True) 
# concat = concatena os dfs e ignore_index mantém a sequência de índices contínua
print(f"\n{dados.shape}")
print(dados.head())
print(dados["Company"].value_counts())

dados['Date'] = pd.to_datetime(dados['Date'])
print(f"\n{dados.dtypes}")

dados.to_csv("Dados tratados/FAANG_consolidado.csv", index=False)