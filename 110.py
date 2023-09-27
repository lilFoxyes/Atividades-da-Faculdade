def somatorio_diagonal_impares(matriz):
    somatorio = 0
    for i in range(len(matriz)):
        if i % 2 == 0:
            somatorio += matriz[i][i]
    return somatorio

def main():
    matriz_A = []
    for _ in range(5):
        linha = input("Digite os 5 elementos da linha separados por espaços: ").split()
        linha = [int(elemento) for elemento in linha]
        matriz_A.append(linha)

    resultado = somatorio_diagonal_impares(matriz_A)

    print("O somatório dos elementos nas posições de linha e coluna ímpares da diagonal principal é: {}".format(resultado))

if __name__ == "__main__":
    main()
