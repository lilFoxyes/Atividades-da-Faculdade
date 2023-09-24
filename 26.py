valor1 = 0.6
valor2 = 0.48
valor3 = 1.29

valor = float(input("Digite o seu consumo em KW/h: "))

tipo = int(input("Digite o número do seu tipo de cliente: "))

if tipo == 1:
    conta = valor * valor1
    print("A sua conta no mês será de: {:.2f} dinheiros.".format(conta))

elif tipo == 2:
    conta = valor * valor2
    print("A sua conta no mês será de: {:.2f} dinheiros.".format(conta))

elif tipo == 3:
    conta = valor * valor3
    print("A sua conta no mês será de: {:.2f} dinheiros.".format(conta))

else:
    print("Digite um tipo de cliente válido!")