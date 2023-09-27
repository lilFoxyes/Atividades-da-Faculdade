def ler_matriz():
    matriz = []
    for _ in range(5):
        linha = input().split()
        matriz.append([float(x) for x in linha])
    return matriz

def calcular_somatorio_acima_diagonal_secundaria(matriz):
    soma = 0
    for i in range(5):
        for j in range(4 - i):
            soma += matriz[i][j]
    return soma

def main():
    matriz_A = ler_matriz()

    somatorio_acima_diagonal_secundaria = calcular_somatorio_acima_diagonal_secundaria(matriz_A)

    print("Somatório dos elementos acima da diagonal secundária da matriz: {:.2f}".format(somatorio_acima_diagonal_secundaria))

if __name__ == "__main__":
    main()