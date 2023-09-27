def ler_matriz():
    matriz = []
    for i in range(4):
        linha = input().split()
        matriz.append([int(x) for x in linha])
    return matriz

def somar_diagonal_principal(matriz):
    soma = 0
    for i in range(4):
        soma += matriz[i][i]
    return soma

def main():
    print("Digite os elementos da matriz A:")
    matriz_A = ler_matriz()

    soma_diagonal = somar_diagonal_principal(matriz_A)

    print("Somatório dos elementos da diagonal principal da matriz A: {}".format(soma_diagonal))

if __name__ == "__main__":
    main()