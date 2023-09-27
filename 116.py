matriz_a = []
entrada_a = input().split(',')

for elemento in entrada_a:
    matriz_a.append(int(elemento))


matriz_b = []
entrada_b = input().split(',')

for elemento in entrada_b:
    matriz_b.append(int(elemento))

matriz_c = []

for i in range(12):
    elemento_c1 = matriz_a[i] * 2
    elemento_c2 = matriz_b[i] - 5
    matriz_c.append([elemento_c1, elemento_c2])


for i in range(12):
    print("{:<5} {:<5}".format(matriz_c[i][0], matriz_c[i][1]))