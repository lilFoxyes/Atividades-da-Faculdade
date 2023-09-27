def criar_matriz(linhas, colunas):
    matriz = []
    for i in range(linhas):
        linha = []
        for j in range(colunas):
            linha.append(0)
        matriz.append(linha)
    return matriz

def exibir_matriz(matriz):
    for linha in matriz:
        for elemento in linha:
            print(elemento, end=' ')
        print()

def transformar_matriz(matriz):
    linhas = len(matriz)
    colunas = len(matriz[0])

    for i in range(linhas):
        for j in range(colunas):
            if matriz[i][j] % 2 == 0:
                matriz[i][j] += 5
            else:
                matriz[i][j] -= 4

def main():
    linhas = int(input().split()[0])
    colunas = int(input().split()[0])

    matriz_A = criar_matriz(linhas, colunas)

    for i in range(linhas):
        entrada = input().split()
        for j in range(colunas):
            matriz_A[i][j] = int(entrada[j])

    print("Matriz A:")
    exibir_matriz(matriz_A)

    matriz_B = criar_matriz(linhas, colunas)

    for i in range(linhas):
        for j in range(colunas):
            matriz_B[i][j] = matriz_A[i][j]

    transformar_matriz(matriz_B)

    print("Matriz B após transformação:")
    exibir_matriz(matriz_B)

if __name__ == "__main__":
    main()