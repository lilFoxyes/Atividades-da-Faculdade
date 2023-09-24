import string



while True:
    a = input("Deseja comprar algum carro com desconto? ")

    if a == "Sim":
        comb = input("Digite se o carro é movido à álcool, à gasolina ou à diesel e cacularei o desconto: ")
        
        if comb == "álcool":
            alcool = int(input("Digite o valor do carro: "))
            if alcool == 0:
                print("Pensei que queria comprar um carro, volte sempre.")
                break
            disc_alcool = alcool * 0.75
            print("O valor desse carro é: {} dinheiros".format(disc_alcool))
            
        
            
        
        elif comb == "gasolina":
            gasolina = int(input("Digite o valor do carro: "))
            if gasolina == 0:
                print("Pensei que queria comprar um carro, volte sempre.")
                break
            disc_gasolina = gasolina * 0.79
            print("O valor desse carro é: {} dinheiros".format(disc_gasolina))
           
            

        elif comb == "diesel":
            diesel = int(input("Digite o valor do carro: "))
            if diesel == 0:
                print("Pensei que queria comprar um carro, volte sempre.")
                break
            disc_diesel = diesel * 0.86
            print("O valor desse carro é: {} dinheiros".format(disc_diesel))
            

        else:
            print("Digite qual é o trem do carro que gostaria de comprar!")    


    
    elif a == "Não":
        print("Obrigado por nos visitar, volte sempre!")
        break
    
    else:
        print("Digite Sim ou Não, qualquer outro comando não será aceito!")

