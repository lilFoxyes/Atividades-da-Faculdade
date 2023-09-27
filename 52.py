votos_candidato_1 = 0
votos_candidato_2 = 0
votos_candidato_3 = 0
votos_nulos = 0
votos_brancos = 0
total_eleitores = 10525
total_votantes = 0


while True:
    codigo_voto = int(input("Digite o código do candidato (1, 2, 3), 4 para nulo, 5 para branco, ou 0 para encerrar a eleição: "))


    if codigo_voto == 0:
        break  

    if codigo_voto == 1:
        votos_candidato_1 += 1
    
    elif codigo_voto == 2:
        votos_candidato_2 += 1
    
    elif codigo_voto == 3:
        votos_candidato_3 += 1
    
    elif codigo_voto == 4:
        votos_nulos += 1
    
    elif codigo_voto == 5:
        votos_brancos += 1

    total_votantes += 1


percentual_candidato_1 = (votos_candidato_1 / total_votantes) * 100
percentual_candidato_2 = (votos_candidato_2 / total_votantes) * 100
percentual_candidato_3 = (votos_candidato_3 / total_votantes) * 100


if votos_candidato_1 > votos_candidato_2 and votos_candidato_1 > votos_candidato_3:
    candidato_vencedor = 1

elif votos_candidato_2 > votos_candidato_1 and votos_candidato_2 > votos_candidato_3:
    candidato_vencedor = 2

else:
    candidato_vencedor = 3


nao_votaram = total_eleitores - total_votantes

print("Candidato vencedor: Candidato {}".format(candidato_vencedor))
print("Total de votos nulos: {}".format(votos_nulos))
print("Total de votos em branco: {}".format(votos_brancos))
print("Total de pessoas que não votaram: {}".format(nao_votaram))
print("Percentual de votos do Candidato 1: {:.2f}%".format(percentual_candidato_1))
print("Percentual de votos do Candidato 2: {:.2f}%".format(percentual_candidato_2))
print("Percentual de votos do Candidato 3: {:.2f}%".format(percentual_candidato_3))