matriz_a = []
matriz_b = []

valor_a = 12
for i in range(4):
    linha_a = []
    for j in range(5):
        linha_a.append(valor_a)
        valor_a += 12
    matriz_a.append(linha_a)

valor_b = 30
for i in range(4):
    linha_b = []
    for j in range(5):
        linha_b.append(valor_b)
        valor_b += 30
    matriz_b.append(linha_b)

matriz_c = []

for i in range(4):
    linha_c = []
    for j in range(5):
        diferenca = matriz_a[i][j] - matriz_b[i][j]
        linha_c.append(diferenca)
    matriz_c.append(linha_c)

for i in range(4):
    for j in range(5):
        print("{:4d} ".format(matriz_c[i][j]), end="")
    print()