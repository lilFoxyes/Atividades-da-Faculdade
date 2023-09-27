

numero = int(input("Digite um número inteiro: "))

def eh_numero_primo(numero):
    if numero <= 1:
        return False

    for i in range(2, numero):
        if numero % i == 0:
            return False

    return True

if eh_numero_primo(numero):
    print("{} é um número primo.".format(numero))
else:
    print("{} não é um número primo.".format(numero))