
pesos_times = []
idades_times = []
total_peso = 0
total_idade = 0

for i in range(40):
    print("Time {}:".format(i + 1))
    
    pesos_time = []
    idades_time = []

    for j in range(23):
        jogador = input("Digite o peso e a idade do jogador {} (separados por espaço): ".format(j + 1)).split()
        peso = float(jogador[0])
        idade = int(jogador[1])

        pesos_time.append(peso)
        idades_time.append(idade)

        total_peso += peso
        total_idade += idade

    media_peso_time = sum(pesos_time) / len(pesos_time)
    media_idade_time = sum(idades_time) / len(idades_time)

    pesos_times.append(media_peso_time)
    idades_times.append(media_idade_time)

media_peso_total = total_peso / (40 * 23)
media_idade_total = total_idade / (40 * 23)

for i in range(40):
    print("Time {} - Média de Peso: {:.2f}, Média de Idade: {:.2f}".format(i + 1, pesos_times[i], idades_times[i]))

print("Média de Peso de Todos os Jogadores: {:.2f}".format(media_peso_total))
print("Média de Idade de Todos os Jogadores: {:.2f}".format(media_idade_total))