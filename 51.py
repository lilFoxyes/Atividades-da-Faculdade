dados = []
salario = []
altura_mulheres_80kg = []
peso_homens = []
altura_mulheres = []
altura_homens = []
contadorDF = 0
contador_de_baixinhos = 0
contador_de_baixinhas = 0

for i in range(10):
    nome, sexo, uf, idade, peso, altura, salario_12_meses = input("Digite o nome, sexo, uf, idade, peso, altura, e o salário dos últimos 12 meses: ").split()
    idade = int(idade)
    peso = float(peso)
    altura = float(altura)
    salario_12_meses = float(salario_12_meses)
    dados.append((nome, sexo, uf, idade, peso, altura, salario_12_meses))
    salario.append(salario_12_meses)

    if len(salario) > 10:
        salario.pop(0)

    media_salario = sum(salario) / len(salario)
    print("A média dos últimos 10 salários inseridos é: {:.2f}".format(media_salario))

maior_salario = max(salario)
for nome, _, _, _, _, _, salario_12_meses in dados:
    if salario_12_meses == maior_salario:
        print("O maior salário é de {} e recebe {:.2f} dinheiros".format(nome, salario_12_meses))

for nome, sexo, uf, idade, peso, altura, salario_12_meses in dados:
    if sexo == "feminino" and peso > 80:
        altura_mulheres_80kg.append(altura)

    if sexo == "masculino" and 1.60 <= altura <= 1.80:
        peso_homens.append(peso)

    if sexo == "feminino" and 1.55 <= altura <= 1.70:
        altura_mulheres.append(altura)

    if sexo == "masculino" and 1.65 <= altura <= 1.80:
        altura_homens.append(altura)

    if uf == "DF":
        contadorDF += 1    

media_altura_mulheres = sum(altura_mulheres_80kg) / len(altura_mulheres_80kg)

media_peso_homens = sum(peso_homens) / len(peso_homens)

media_altura_mulheres_baixinhas = sum(altura_mulheres) / len(altura_mulheres)

media_altura_homens_baixinhos = sum(altura_homens) / len(altura_homens)

for _, sexo, _, _, _, altura, _ in dados:
    if sexo == "feminino" and 1.55 <= altura <= 1.70:
        contador_de_baixinhas += 1

    if sexo == "masculino" and 1.65 <= altura <= 1.80:
        contador_de_baixinhos += 1

total_de_baixinhos = contador_de_baixinhos + contador_de_baixinhas

porcentagem_baixinhos = (total_de_baixinhos / len(dados)) * 100

print("A porcentagem de pessoas consideradas de estatura mediana é {:.2f}%".format(porcentagem_baixinhos))

print("A média da altura das mulheres com mais de 80kg é: {:.2f}m".format(media_altura_mulheres))

print("A média de peso dos homens com altura entre 1.60m e 1.80m é: {:.2f}kg".format(media_peso_homens))

print("A média de altura das mulheres com altura entre 1.55m e 1.70m é: {:.2f}m".format(media_altura_mulheres_baixinhas))

print("A média de altura dos homens com altura entre 1.65m e 1.80m é: {:.2f}m".format(media_altura_homens_baixinhos))

print("O total de residentes no DF é: {}".format(contadorDF))