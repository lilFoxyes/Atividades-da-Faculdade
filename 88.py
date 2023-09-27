A = [0] * 15
B = [0] * 15


print("Digite os elementos da matriz A:")
for i in range(15):
    A[i] = int(input("Elemento {}: ".format(i + 1)))


print("Digite os elementos da matriz B:")
for i in range(15):
    B[i] = int(input("Elemento {}: ".format(i + 1)))


C = A + B


print("Matriz C (junção das matrizes A e B):")
for i, elemento in enumerate(C):
    print("Elemento {}: {}".format(i + 1, elemento))