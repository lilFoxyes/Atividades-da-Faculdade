dados = []
contador_porquinho = 0

for i in range (10):
    peso_porquinho = float(input("Digite o peso do porquinho {}: ".format(i + 1)))
    dados.append(peso_porquinho)

media_peso_porquinho = sum(dados) / len(dados)
maior_porquinho = max(dados)
for peso in dados:
    if peso > maior_porquinho:
        maior_porquinho = peso

    elif peso > media_peso_porquinho:
        contador_porquinho += 1


print("O porquinho mais pesado tem {} kg e tem {} porquinho(s) acima do peso.".format(maior_porquinho, contador_porquinho))