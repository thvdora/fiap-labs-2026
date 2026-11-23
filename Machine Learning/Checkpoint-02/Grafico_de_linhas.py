import matplotlib.pyplot as plt
import numpy as np

## dados do dashboard
# Desafio 1: Deployments realizados por mês (Histórico do Ano)
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
deploys_2023 = [12, 15, 14, 21, 28, 30, 25, 32, 40, 38, 45, 52]

## Gráfico de linha
x = meses
y = deploys_2023

plt.plot(x, y, color='purple', linestyle='--', marker='x')
plt.xticks(rotation=45)
plt.grid(True, linestyle=':', alpha=0.6, linewidth=0.5, color='gray')
plt.title('Quantidade de Deploys por Mês em 2023')
plt.show()