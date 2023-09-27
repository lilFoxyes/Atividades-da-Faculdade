vetor = [0] * 30


print("Digite 30 valores para preencher o vetor:")
for i in range(30):
    vetor[i] = float(input("Elemento {}: ".format(i + 1)))


x = float(input("Digite o número que deseja buscar: "))


if x in vetor:
    print("{:.2f} existe no vetor.".format(x))
else:
    print("{:.2f} não existe no vetor.".format(x))