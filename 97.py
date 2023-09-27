matriz_a = []
matriz_b = []


contador = 1
while len(matriz_a) < 10:
    if contador % 2 == 0 and contador % 3 == 0:
        matriz_a.append(contador)
    contador += 1


contador = 1
while len(matriz_b) < 10:
    if contador % 5 == 0:
        matriz_b.append(contador)
    contador += 1


matriz_c = matriz_a + matriz_b


if len(matriz_c) == 20:

    print("Matriz C (contendo 20 elementos):")
    for elemento in matriz_c:
        print(elemento, end=" ")
else:
    print("Não foi possível criar uma matriz C com 20 elementos.")
    