total_verdes = 0
total_amarelos = 0
total_rosa = 0
total_M = 0
total_GG = 0
total_maior150 = 0
total_menor80 = 0

for i in range(10):
    tamanho, cor, preco = input("Digite o tamanho, a cor e o preço da peça: ").split()
    preco = int(preco)

    if tamanho == "M":
        total_M += 1

    if tamanho == "GG":
        total_GG += 1

    if cor == "rosa":
        total_rosa += 1

    if cor =="verde":
        total_verdes += 1

    if cor == "amarelo":
        total_amarelos += 1

    if preco > 150:
        total_maior150 += 1

    if 80 > preco:
        total_menor80 += 1

print("O total de verdes é: {}".format(total_verdes))
print("O total de amarelos é: {}".format(total_amarelos))
print("O total de rosas é: {}".format(total_rosa))
print("O total de M é: {}".format(total_M))
print("Total GG é: {}".format(total_GG))
print("O total de maior que 150 é: {}".format(total_maior150))
print("O total de menor do que 80 é: {}".format(total_menor80))

