matriz_estados = []

for i in range(26):
    estado = input("Digite o nome do estado: ")
    matriz_municipios = []

    for j in range(10):
        municipio = input("Digite o nome do município {} do estado {}: ".format(j+1, estado))
        populacao = int(input("Digite a população do município {}: ".format(municipio)))
        matriz_municipios.append([municipio, populacao])

    matriz_estados.append([estado, matriz_municipios])

municipio_mais_populoso = ""
populacao_mais_populosa = 0
estado_mais_populoso = ""

soma_populacao_capitais = 0

for estado, municipios in matriz_estados:
    capital_populacao = municipios[0][1]
    soma_populacao_capitais += capital_populacao

    if capital_populacao > populacao_mais_populosa:
        populacao_mais_populosa = capital_populacao
        municipio_mais_populoso = municipios[0][0]
        estado_mais_populoso = estado

print("O município mais populoso é {} no estado de {}".format(municipio_mais_populoso, estado_mais_populoso))

media_populacao_capitais = soma_populacao_capitais / 26
print("A média da população das capitais dos estados é {:.2f}".format(media_populacao_capitais))