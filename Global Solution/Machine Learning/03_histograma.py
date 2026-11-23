import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("Dados tratados/FAANG_consolidado.csv")

plt.figure(figsize=(10, 6))

plt.hist(
    dados['Volume'],
    bins=10,
    color='#287C8E',
    edgecolor='white',
    linewidth=1.2,
    alpha=0.9
)

plt.title('Distribuição do Volume Negociado - FAANG',
          fontsize=14, fontweight='bold', pad=15)

plt.xlabel('Volume Negociado (ações)', fontsize=11)
plt.ylabel('Frequência', fontsize=11)

plt.grid(axis='y', linestyle='--', alpha=0.25)

plt.tight_layout()
plt.show()