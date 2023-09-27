total_espectadores = 100
respostas_otima = 0
respostas_bom = 0
respostas_regular = 0
respostas_ruim = 0
respostas_pessimo = 0
idades_ruim = []
idades_pessimo = []
maior_idade_pessimo = 0
maior_idade_otimo = 0


for _ in range(total_espectadores):
    idade = int(input("Qual é a sua idade? "))
    opniao = int(input("Qual é a sua opinião sobre o filme (de 1 a 5)? "))

    
    if opniao == 5:
        respostas_otima += 1
        if idade > maior_idade_otimo:
            maior_idade_otimo = idade
    elif opniao == 4:
        respostas_bom += 1
    elif opniao == 3:
        respostas_regular += 1
    elif opniao == 2:
        respostas_ruim += 1
        idades_ruim.append(idade)
    elif opniao == 1:
        respostas_pessimo += 1
        idades_pessimo.append(idade)
        if idade > maior_idade_pessimo:
            maior_idade_pessimo = idade


percentual_bom_ruim = ((respostas_bom - respostas_ruim) / total_espectadores) * 100
media_idades_ruim = sum(idades_ruim) / len(idades_ruim) if idades_ruim else 0
percentual_pessimo = (respostas_pessimo / total_espectadores) * 100

print("Quantidade de respostas ótimas:", respostas_otima)
print("Diferença percentual entre respostas bom e ruim:", percentual_bom_ruim)
print("Média de idade das pessoas que responderam ruim:", media_idades_ruim)
print("Percentagem de respostas péssimo:", percentual_pessimo)
print("Maior idade de quem respondeu péssimo:", maior_idade_pessimo)
print("Diferença de idade entre a maior idade que respondeu ótimo e a maior idade que respondeu ruim:",
      maior_idade_otimo - maior_idade_pessimo)