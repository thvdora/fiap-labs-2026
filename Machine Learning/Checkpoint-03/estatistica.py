# Exercicio 1: Tempos de atendimento

tempos_atendimento = [12, 15, 12, 18, 20, 12, 22, 15, 18, 16]

# Funções
def calcular_media(lista):
    if not lista:
        return 0  # Retorna 0 se a lista estiver vazia
    return sum(lista) / len(lista)

def calcular_mediana(lista):
    lista_ordenada = sorted(lista)
    n = len(lista_ordenada)
    meio = n // 2

    if n % 2 != 0:
        return lista_ordenada[meio]
    else:
        return (lista_ordenada[meio - 1] + lista_ordenada[meio] / 2)

def calcular_moda(lista):
    frequencia = 0
    valor_moda = None

    for i in range(len(lista)):
        contador = 0

        for j in range(len(lista)):
            if lista[i] == lista[j]:
                contador += 1

        if contador > frequencia:
            frequencia = contador
            valor_moda = lista[i]
    return valor_moda

# Resultado
media = calcular_media(tempos_atendimento)
print(f"A média do tempo de atendimento é de: {media:.0f} minutos")

mediana = calcular_mediana(tempos_atendimento)
print(f"A mediana é: {mediana}")

moda = calcular_moda(tempos_atendimento)
print(f"A moda do tempo de atendimento é: {moda}")

# Exercício 2: Variância e desvio padrão

# Funções
def calcular_variancia(lista):
    soma_quadrados = sum((x - media) ** 2 for x in lista)
    n = len(lista)
    variacao = soma_quadrados / len(lista)
    return variacao

def calcular_desvio(lista):
    desvio = calcular_variancia(lista) ** 0.5
    return desvio

# Resultado
variancia = calcular_variancia(tempos_atendimento)
print(f"A variância do tempo dos atendimentos é de: {variancia:.2f}")

desvio_padrao = calcular_desvio(tempos_atendimento)
print(f"O desvio padrão é: {desvio_padrao:.2f}")

# Exercício 3: Comparação de desempenho

Turma_A = [7.0, 7.5, 8.0, 7.0, 8.5, 9.0, 7.0, 8.0]
Turma_B = [5.0, 9.5, 6.0, 10.0, 5.5, 9.0, 6.5, 10.5]

print(f"A média da turma A é: {calcular_media(Turma_A)}")
print(f"Desvio padrão: {calcular_desvio(Turma_A):.2f}")
print(f"A média da turma B é: {calcular_media(Turma_B)}")
print(f"Desvio padrão: {calcular_desvio(Turma_B):.2f}")