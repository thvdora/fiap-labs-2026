import matplotlib.pyplot as plt
import numpy as np

# Desafio 2: Número de Bugs resolvidos por Tecnologia da equipe
tecnologias = ['Python', 'JavaScript', 'Java', 'TypeScript', 'Go']
bugs_resolvidos = [45, 68, 32, 55, 18]

## Gráfico de barras
x = bugs_resolvidos
y = tecnologias

plt.bar(y, x, color='orange', alpha=0.7)
plt.xlabel(bugs_resolvidos)
plt.ylabel(tecnologias)
plt.title('Número de Bugs Resolvidos por Tecnologia')

## Mostrar os valores em cima de cada barra como foi pedido no desafio 2
for i, v in enumerate(x):
    plt.text(i, v + 1, str(v), ha='center', va='bottom') ## ha = horizontal alignment, va = vertical alignment
    ## v + 1 é para colocar o texto um pouco acima da barra, para não ficar em cima da barra
plt.ylim(0, max(x) + 10)  # Ajusta o limite do eixo y para dar espaço para os valores

plt.show()