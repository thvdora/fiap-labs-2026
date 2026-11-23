numero = int(input("Digite um número: "))

# criar uma variavel para guardar a soma
# i = 1
# enquanto i <= n:
# verifico com if se o número é impar usando % 
# se for impar, adiciono na variavel de somas
# i++ para continuar rodando o loop
# retorno

soma_impares = 0
i = 1

while i <= numero:
    if i % 2 != 0:
        soma_impares += i
    i += 1
print(soma_impares)

# criar uma variavel para guardar os multiplos
# usar um for de i até numero:
# i % 3 e verifico se == 0 and i % 2 == 0.b se for, conto na variavel multiplos

multiplos = 0
for i in range(1, numero + 1):
    if i % 3 == 0 and i % 2 == 0:
        multiplos += 1
print(multiplos)