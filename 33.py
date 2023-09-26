
nome, idade, grupo = input("Digite o seu nome, a sua idade, e o grupo de risco (baixo, médio ou alto) para avaliarmos a categoria disponível no seguro: ").split()

idade = int(idade)



if 20 >= idade >= 17:
    if grupo == "baixo":
        categoria = 1

    elif grupo == "médio":
        categoria = 2

    elif grupo == "alto":
        categoria = 3

    else:
        print("Digite um grupo válido")

    print("{} com {} anos de idade está na categoria {}".format(nome, idade, categoria))    

elif 24 >= idade >= 21:
    if grupo == "baixo":
        categoria = 2

    elif grupo == "médio":
            categoria = 3

    elif grupo == "alto":
        categoria = 4

    else:
        print("Digite um grupo válido")

    print("{} com {} anos de idade está na categoria {}".format(nome, idade, categoria))    

elif 34 >= idade >= 25:
    if grupo == "baixo":
        categoria = 3

    elif grupo == "médio":
        categoria = 4

    elif grupo == "alto":
        categoria = 5

    else:
        print("Digite um grupo válido")

    print("{} com {} anos de idade está na categoria {}".format(nome, idade, categoria))    

elif 64 >= idade >= 35:
    if grupo == "baixo":
        categoria = 4

    elif grupo == "médio":
        categoria = 5

    elif grupo == "alto":
        categoria = 6

    else:
        print("Digite um grupo válido")

    print("{} com {} anos de idade está na categoria {}".format(nome, idade, categoria))    

elif 70 >= idade >= 65:
    if grupo == "baixo":
        categoria = 7

    elif grupo == "médio":
        categoria = 8

    elif grupo == "alto":
        categoria = 9

    else:
        print("Digite um grupo válido")

    print("{} com {} anos de idade está na categoria {}".format(nome, idade, categoria))    
                                                

            

else:
    print("Não está no intervalo necessário para adquirir um seguro!")

        


