
nome, sexo, altura, idade = input("Digite o seu nome, sexo (f ou m), altura (com ponto), idade e irei lançar o seu peso ideal: ").split()
altura = float(altura)
idade = int(idade)

if sexo == "m":
    
    if altura > 170:
        if 20 >= idade:
            peso_ideal = (72.7 * altura) - 58
        elif 39 >= idade >= 21:
            peso_ideal = (72.7 * altura) - 53
        elif idade >= 40:
            peso_ideal = (72.7 * altura) - 45

    elif 170 >= altura:
        if 40 >= idade:
            peso_ideal = (72.7 * altura) - 50
        elif idade > 40:
            peso_ideal = (72.7 * altura) - 58

elif sexo == "f":
    if altura > 150:
        peso_ideal = (62.1 * altura) - 44.7
    elif 150 >= altura:
        if idade >= 35:
            peso_ideal = (62.1 * altura) - 45
        elif 35 > idade:
            peso_ideal = (62.1 * altura) - 49
else:
    print("Digita certo aí, fazendo favor")            


print("{}, o seu peso ideial é: {:.2f}kg".format(nome, peso_ideal))                                             

        


