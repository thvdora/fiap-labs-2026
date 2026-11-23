import numpy as np

# Crie o array dados_temperatura aqui
dados_temperatura = np.array([20, 21, 22, 23, 24, 25, 26, 27, 28, 29])

# Calcule e imprima a média 
temperatura_media = np.mean(dados_temperatura)
print("Temperatura média:", temperatura_media)

# Calcule e imprima a temperatura máxima
temperatura_maxima = np.max(dados_temperatura)
print("Temperatura máxima:", temperatura_maxima)

# Calcule e imprima quantos dias a temperatura foi superior a 25
dias_superior_25 = np.sum(dados_temperatura > 25)
print("Dias com temperatura superior a 25°C:", dias_superior_25)