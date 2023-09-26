dados = []
altura_mulheres = []
peso_homens = []

for i in range(5):
    nome, peso, altura, sexo = input("Digite o seu nome, peso, altura e sexo: ").split()
    peso = float(peso)
    altura = float(altura)
    dados.append((nome, peso, altura, sexo))

for nome, peso, altura, sexo in dados:
    if sexo == "feminino":
        altura_mulheres.append(altura)
    
    if sexo == "masculino":
        peso_homens.append(peso)

media_altura_mulheres = sum(altura_mulheres) / len(altura_mulheres)
media_peso_homens = sum(peso_homens) / len(peso_homens)

print("A média da altura feminina é {:.2f}".format(media_altura_mulheres))
print("A média do peso masculino é {:.2f}kg".format(media_peso_homens))

for nome, peso, altura, sexo in dados:
    if sexo == "feminino" and altura > media_altura_mulheres:
        print("{} tem {:.2f} e é mais alta que a média das mulheres.".format(nome, altura))

for nome, peso, altura, sexo in dados:
    if sexo == "feminino" and altura == max(altura for nome, _, altura, _ in dados):
        print("A mais alta é a {} com {:.2f} de altura".format(nome, altura))

for nome, peso, altura, sexo in dados:
    if sexo == "masculino" and peso < media_peso_homens:
        print("{} está abaixo da média de peso dos homens e pesa {:.2f}kg".format(nome, peso))

for nome, peso, _, _ in dados:
    if peso == max(peso for _, peso, _, _ in dados):
        print("{} é o mais pesado e pesa {:.2f}kg".format(nome, peso))


        
    
