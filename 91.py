def calcular_fatorial(n):
    if n == 0:
        return 1
    else:
        fatorial = 1
        for i in range(1, n + 1):
            fatorial *= i
        return fatorial


vetor_a = [5, 3, 7, 2, 8, 4, 10, 6, 1, 9, 15, 13, 11, 12, 14]


vetor_b = []


for elemento in vetor_a:
    fatorial = calcular_fatorial(elemento)
    vetor_b.append(fatorial)


print("Vetor B (Fatoriais de A):")
for i in range(len(vetor_b)):
    print("Elemento {}: {}".format(i + 1, vetor_b[i]))