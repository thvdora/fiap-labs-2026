# Guardando o input do usuário e criando a matriz 3x4
matriz = []

for i in range(3):
    linha = []
    for j in range(4):
        temperatura = float(input(f"Digite a temperatura [{i}][{j}]: "))
        linha.append(temperatura)
    matriz.append(linha)

print(matriz)

# Calculando a média semanal das temperaturas
def media_semanal(matriz):
    medias = []
    
    for i in range(len(matriz)):
        media = sum(matriz[i]) / len(matriz[i])
        medias.append(media)
    
    return medias

# Formatando a saída final de médias
medias = media_semanal(matriz)
# enumerate rastreia o índice e o valor de cada elemento ao mesmo tempo
for i, media in enumerate(medias): 
    print(f"Média da semana {i + 1}: {media:.2f}")

# Pegando a maior e menor temperatura registrada
maior_temp = matriz[0][0] 
menor_temp = matriz[0][0]

for i in range(len(matriz)):
   for j in range(len(matriz[i])):
    if matriz[i][j] > maior_temp:
        maior_temp = matriz[i][j]
    if matriz[i][j] < menor_temp:
        menor_temp = matriz[i][j]

print(f"A maior temperatura registrada é: {maior_temp:.2f}")
print(f"A menor temperatura registrada é: {menor_temp:.2f}")