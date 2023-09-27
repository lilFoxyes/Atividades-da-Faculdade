

numero = int(input("Digite um número inteiro: "))

def eh_numero_perfeito(numero):
    soma_divisores = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma_divisores += i
    return soma_divisores == numero


if eh_numero_perfeito(numero):
    print("{} é um número perfeito.".format(numero))
else:
    print("{} não é um número perfeito.".format(numero))