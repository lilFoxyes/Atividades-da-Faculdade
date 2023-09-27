soma = 0
numerador = 1
denominador = 1

for i in range(1, 51):
    soma += numerador / denominador
    numerador += 2
    denominador += 1

print("Soma:", soma)