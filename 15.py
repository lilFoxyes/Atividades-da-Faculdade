contador1 = 0
contador2 = 0
for i in range (5):
    nome, sexo, idade, saude = input("Digite o seu nome, sexo, idade e estado de saúde (saudável ou doente) e te direi se pode servir no serviço obrigatório: ").split()
    if sexo == "masculino" and int(idade) > 18 and saude == "saudável":
        print("Parabéns, {}, você está apto para o serviço militar obrigatório!".format(nome))
        contador1 += 1
    elif sexo == "feminino":
        print("{}, infelizmente você não está apto para o serviço militar obrigatório, caso esteja interessada, pode tentar ingressar por meio de um concurso público".format(nome)) 
        contador2 += 1
    else:
        print("{}, infelizmente você não está apto para o serviço militar obrigatório, caso esteja interessado, pode tentar ingressar por meio de um concurso público".format(nome))
        contador2 += 1
total = contador2 + contador1

print("A quantidade total de pessoas inscritas foi {}, do total de inscritos {} estavam aptos para servir e {} estavam inaptos.".format(total, contador1, contador2))

