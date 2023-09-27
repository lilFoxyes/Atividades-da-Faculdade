total_entrevistados = 2000
respostas = []
sexo_feminino = 0
sexo_masculino = 0
respondeu_sim = 0
respondeu_nao = 0

for i in range(total_entrevistados):
    sexo, resposta = input("Digite o sexo (M/F) e a resposta (Sim/Não) do entrevistado (separados por espaço): ").split()
    respostas.append(resposta.lower())
    
    if sexo.lower() == 'f':
        sexo_feminino += 1
        if resposta.lower() == 'sim':
            respondeu_sim += 1
    elif sexo.lower() == 'm':
        sexo_masculino += 1
        if resposta.lower() == 'não':
            respondeu_nao += 1

percentual_feminino_sim = (respondeu_sim / sexo_feminino) * 100 if sexo_feminino > 0 else 0
percentual_masculino_nao = (respondeu_nao / sexo_masculino) * 100 if sexo_masculino > 0 else 0

print("Número de pessoas que responderam Sim: {}".format(respostas.count('sim')))
print("Número de pessoas que responderam Não: {}".format(respostas.count('não')))
print("Porcentagem de mulheres que responderam Sim: {:.2f}%".format(percentual_feminino_sim))
print("Porcentagem de homens que responderam Não: {:.2f}%".format(percentual_masculino_nao))