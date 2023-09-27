def ler_matriz():
    matriz = []
    for _ in range(15):
        linha = input().split()
        matriz.append([int(x) for x in linha])
    return matriz

def calcular_media(matriz):
    soma = 0
    total_elementos = 0
    for linha in matriz:
        for elemento in linha:
            soma += elemento
            total_elementos += 1
    media = soma / total_elementos
    return media

def somar_elementos_pares_diagonal_principal(matriz):
    soma = 0
    for i in range(15):
        if matriz[i][i] % 2 == 0:
            soma += matriz[i][i]
    return soma

def main():
    print("Digite os elementos da matriz A:")
    matriz_A = ler_matriz()

    media_elementos = calcular_media(matriz_A)
    soma_pares_diagonal = somar_elementos_pares_diagonal_principal(matriz_A)

    print("Média de todos os elementos da matriz: {:.2f}".format(media_elementos))
    print("Somatório dos elementos pares na diagonal principal: {}".format(soma_pares_diagonal))

if __name__ == "__main__":
    main()