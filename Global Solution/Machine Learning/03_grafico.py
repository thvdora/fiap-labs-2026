import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dados = pd.read_csv("Dados tratados/FAANG_consolidado.csv")

dados['Date'] = pd.to_datetime(dados['Date'])
dados = dados.sort_values('Date')

plt.figure(figsize=(12, 6))

cores = sns.color_palette('husl', 5)
empresas = dados.groupby('Company')
for i, (nome, grupo) in enumerate(empresas):
    plt.plot(
        grupo['Date'],
        grupo['Close'],
        label=nome,
        color=cores[i],
        linewidth=2
    )

plt.title('Preços de Fechamento ao Longo do Tempo - FAANG', fontsize=14, fontweight='bold', pad=15)
plt.xlabel('Data', fontsize=11)
plt.ylabel('Preço de Fechamento (USD)', fontsize=11)

plt.legend()
plt.grid(axis='y', linestyle='--', alpha=0.25)

plt.tight_layout()
plt.show()
