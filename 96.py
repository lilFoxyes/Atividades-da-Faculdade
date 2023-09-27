matriz_a = []
matriz_b = []


for i in range(2, 13, 2):
    matriz_a.append(i)


for i in range(1, 12, 2):
    matriz_b.append(i)


matriz_c = matriz_a + matriz_b


if len(matriz_c) == 12:
  
    print("Matriz C (contendo 12 elementos):")
    for elemento in matriz_c:
        print(elemento, end=" ")
else:
    print("Não foi possível criar uma matriz C com 12 elementos.")