matriz = [0] * 10


for i in range(10):
    elemento = int(input("Digite o {}º elemento: ".format(i + 1)))
    matriz[i] = elemento


print("Elementos da matriz:")
for i, elemento in enumerate(matriz):
    print("Elemento {}: {}".format(i + 1, elemento))