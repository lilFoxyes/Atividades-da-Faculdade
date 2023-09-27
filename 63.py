
temperaturas = []

for dia in range(1, 32):
    temperatura = float(input("Digite a temperatura média do dia {}: ".format(dia)))
    temperaturas.append(temperatura)

dias_abaixo_zero = sum(1 for temperatura in temperaturas if temperatura <= 0)
dias_acima_zero = sum(1 for temperatura in temperaturas if temperatura > 0)

print("Número de dias com temperaturas menores ou iguais a zero: {}".format(dias_abaixo_zero))
print("Número de dias com temperaturas maiores do que zero: {}".format(dias_acima_zero))