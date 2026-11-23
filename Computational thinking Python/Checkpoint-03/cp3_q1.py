nomes = ["Pedro", "Aline", "Isabella", "Eduardo", "Beatriz", "Gabi", "Sofia"]
notas = [8.5, 9.0, 7.5, 6.0, 10.0, 9.5, 8.0]

media_da_turma = sum(notas)/len(nomes)

maior_nota = notas[0]
aluno_maior_nota = nomes[0]
for i in range(len(nomes)):
    if notas[i] > maior_nota:
        maior_nota = notas[i]
        aluno_maior_nota = nomes[i]

menor_nota = notas[0]
aluno_menor_nota = nomes[0]
for i in range(len(nomes)):
    if notas[i] < menor_nota:
        menor_nota = notas[i]
        aluno_menor_nota = nomes[i]

acima_da_media = []
for i in range(len(nomes)):
    if notas[i] > media_da_turma:
        acima_da_media.append(nomes[i])

print(f"A média da turma é: {media_da_turma:.2f}")
print(f"A maior nota da turma é a de {aluno_maior_nota}: {maior_nota}")
print(f"A menor nota da turma é a de {aluno_menor_nota}: {menor_nota}")
print(f"Os alunos que estão acima da média são: {acima_da_media}")
