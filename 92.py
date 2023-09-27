matriz_a = [1, 2, 3, 4, 5]
matriz_b = [6, 7, 8, 9, 10]
matriz_c = [11, 12, 13, 14, 15]


matriz_d = []


matriz_d.extend(matriz_a)
matriz_d.extend(matriz_b)
matriz_d.extend(matriz_c)


print("Matriz D (Junção de A, B e C):")
for elemento in matriz_d:
    print(elemento)