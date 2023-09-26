dados = []
idades = []
while True:
    idade, altura = input("Digite a sua idade e a sua altura: ").split()
    idade = int(idade)
    altura = float(altura)

    if idade == 0:
    
        break

    dados.append((idade, altura))
    idades.append(idade)




if not idades:
    print("O programa foi encerrado antes mesmo de colocar as informações")

else:
    alturas = [altura for idade, altura in dados if 50 > idade]
    media_altura = sum(alturas) / len(alturas)
    media_idade = sum(idades) / len(idades)
    print("A média de idade é: {:.2f} e a média de altura das pessoas com menos de 50 anos é: {:.2f}". format(media_idade, media_altura))
