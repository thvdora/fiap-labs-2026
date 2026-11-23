numero = int(input("Digite um número inteiro de 0 a 999: "))

unidade = numero % 10
dezena = (numero // 10) % 10 * 10
centena = (numero // 100) * 100

print(f"Centena: {centena}")
print(f"Dezena: {dezena}") 
print(f"Unidade: {unidade}")