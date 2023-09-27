def ler_matriz():
    matriz = []
    for _ in range(4):
        linha = input().split()
        matriz.append([float(x) for x in linha])
    return matriz

def construir_matriz_e(matriz_a, matriz_b, matriz_c, matriz_d):
    matriz_e = []
    for i in range(4):
        linha_e = []
        for j in range(4):
            if i == 0:
                linha_e.append(matriz_a[i][j] * 2)
            elif i == 1:
                linha_e.append(matriz_b[i][j] * 3)
            elif i == 2:
                linha_e.append(matriz_c[i][j] * 4)
            else:
                linha_e.append(matriz_d[i][j])
        matriz_e.append(linha_e)
    return matriz_e

def main():
    matriz_a = ler_matriz()
    matriz_b = ler_matriz()
    matriz_c = ler_matriz()
    matriz_d = ler_matriz()
    
    matriz_e = construir_matriz_e(matriz_a, matriz_b, matriz_c, matriz_d)

    for linha in matriz_e:
        print(" ".join("{:.2f}".format(elemento) for elemento in linha))

if __name__ == "__main__":
    main()