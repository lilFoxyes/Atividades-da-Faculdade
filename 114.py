matriz_a = []
matriz_b = []

valor_par = 2
valor_impar = 1

for i in range(5):
    linha_a = []
    linha_b = []
    for j in range(6):
        linha_a.append(valor_par)
        linha_b.append(valor_impar)
        valor_par += 2
        valor_impar += 2
    matriz_a.append(linha_a)
    matriz_b.append(linha_b)

matriz_c = []

for i in range(5):
    linha_c = []
    for j in range(6):
        soma_elementos = matriz_a[i][j] + matriz_b[i][j]
        linha_c.append(soma_elementos)
    matriz_c.append(linha_c)

for i in range(5):
    for j in range(6):
        print("{:2d} ".format(matriz_c[i][j]), end="")
    print()