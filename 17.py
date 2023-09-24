import string

contador1 = 0
valor1 = 0
valor2 = 0
valor_total = 0

while True:
    a = input("Deseja comprar algum carro com desconto? ")

    if a == "Sim":
        ano = int(input("Qual o ano do carro? "))
        if ano <= 2000:
            carro_2000 = int(input("Digite o valor do carro: "))
            valor_carro_2000 = carro_2000 * 0.88
            print("O valor desse carro é: {} dinheiros".format(valor_carro_2000))
            contador1 += 1
            valor1 += valor_carro_2000
        elif ano > 2000:
            carro_2001 = int(input("Digite o valor do carro: "))
            valor_carro_2001 = carro_2001 * 0.93
            print("O valor desse carro é: {} dinheiros".format(valor_carro_2001))
            valor2 += valor_carro_2001
    elif a == "Não":
        break
    else:
        print("Digite Sim ou Não, qualquer outro comando não será aceito!")

valor_total = valor1 + valor2

print("A quantidade de carros com o ano de fabricação abaixo dos anos 2000 é {}, o total a ser pago é: {} dinheiros".format(contador1, valor_total))