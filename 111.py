def ler_matriz():
    matriz = []
    for _ in range(6):
        linha = input().split()
        matriz.append([float(x) for x in linha])
    return matriz

def calcular_media_abaixo_diagonal(matriz):
    soma = 0
    elementos = 0
    for i in range(6):
        for j in range(i + 1):
            soma += matriz[i][j]
            elementos += 1
    media = soma / elementos
    return media

def main():
    print("Digite os elementos da matriz A:")
    matriz_A = ler_matriz()

    media_abaixo_diagonal = calcular_media_abaixo_diagonal(matriz_A)

    print("Média dos elementos abaixo da diagonal principal da matriz: {:.2f}".format(media_abaixo_diagonal))

if __name__ == "__main__":
    main()