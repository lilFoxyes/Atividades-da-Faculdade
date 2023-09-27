A = [0] * 10


print("Digite os elementos da matriz A:")
for i in range(10):
    A[i] = float(input("Elemento {}: ".format(i + 1)))


B = [x / 2 for x in A]


print("Matriz A:")
for i, elemento in enumerate(A):
    print("Elemento {}: {:.2f}".format(i + 1, elemento))

print("Matriz B (metade dos elementos de A):")
for i, elemento in enumerate(B):
    print("Elemento {}: {:.2f}".format(i + 1, elemento))