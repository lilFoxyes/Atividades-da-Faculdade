soma = 0
numerador = 37 * 38
denominador = 1

for i in range(1, 38):
    soma += numerador / denominador
    numerador -= 1
    denominador += 1

print("Soma:", soma)