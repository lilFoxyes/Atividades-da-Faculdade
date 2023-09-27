numero = int(input("Digite um número inteiro positivo: "))

def e_triangular(numero):
    i = 1
    produto = 1

    
    while produto <= numero:
        if produto == numero:
            return True  
        i += 1
        produto *= i

    return False 





if e_triangular(numero):
    print("{} é um número triangular.".format(numero))
else:
    print("{} não é um número triangular.".format(numero))