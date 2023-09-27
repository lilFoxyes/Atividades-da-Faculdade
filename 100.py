vetor = [0.0] * 25


for i in range(25):
    vetor[i] = float(input("Digite o {}º elemento: ".format(i + 1)))


print("Vetor original:")
print(vetor)


for i in range(12):
    vetor[i], vetor[24 - i] = vetor[24 - i], vetor[i]


print("Vetor invertido:")
print(vetor)