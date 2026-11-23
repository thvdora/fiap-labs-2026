import matplotlib.pyplot as plt
import numpy as np

# Desafio 3: Complexidade do Código vs Horas gastas para Refatoração
# Cada tupla representa uma tarefa do backlog: (Pontos de Complexidade, Horas Gastas, ID da Tarefa)
pontos_story = [3, 5, 8, 5, 13, 2, 8, 21, 3, 13]
horas_gastas = [6, 12, 22, 10, 36, 4, 18, 55, 8, 32]
tarefas_id = ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10']

## Gráfico de dispersão
x = horas_gastas
y = pontos_story

plt.scatter(x, y, color='red', alpha=0.7)
plt.xlabel('Horas Gastas')
plt.ylabel('Pontos de Complexidade')
# Adicionando rótulos para cada ponto
for i, txt in enumerate(tarefas_id):
    plt.annotate(txt, (x[i], y[i]), textcoords="offset points", xytext=(0,10), ha='center')
    ## .annotate = permite adicionar rótulos aos pontos do gráfico
    ## txt = o texto que será exibido, textcoords = "offset points" = define que o texto será exibido em relação ao ponto, xytext = define a posição do texto em relação ao ponto, ha = horizontal alignment = alinha o texto horizontalmente
    
plt.title('Relação entre Pontos de Story e Tempo de Refatoração')
plt.grid(True, linestyle=':', alpha=0.6, linewidth=0.5, color='gray')
plt.ylim(0, max(y) + 2)  # Ajusta o limite do eixo y para dar espaço para os rótulos
plt.show()