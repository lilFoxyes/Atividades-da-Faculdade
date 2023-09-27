matriz_a = []
matriz_b = []


for i in range(6):
    elemento_a = int(input("Digite o elemento {} da matriz A: ".format(i + 1)))
    elemento_b = int(input("Digite o elemento {} da matriz B: ".format(i + 1)))
    matriz_a.append(elemento_a)
    matriz_b.append(elemento_b)


matriz_c = []
matriz_d = []


for i in range(6):
    if i % 2 == 0:  
        matriz_c.append(matriz_a[i])
        matriz_d.append(matriz_b[i])
    else:  
        matriz_c.append(matriz_b[i])
        matriz_d.append(matriz_a[i])


print("Matriz C (elementos de índice ímpar de A e B):", matriz_c)
print("Matriz D (elementos de índice par de A e B):", matriz_d)