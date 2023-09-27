A = [0] * 20
B = [0] * 20


print("Digite os elementos da matriz A:")
for i in range(20):
    A[i] = int(input("Elemento {}: ".format(i + 1)))


print("Digite os elementos da matriz B:")
for i in range(20):
    B[i] = int(input("Elemento {}: ".format(i + 1)))


C = [A[i] - B[i] for i in range(20)]


print("Matriz C (resultado da subtração de A por B):")
for i, elemento in enumerate(C):
    print("Elemento {}: {}".format(i + 1, elemento))