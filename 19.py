sa = 0
aum = 0

for i in range(5):
    nome, salario = input("Digite o seu nome e o seu salário e irei calcular o reajuste que a empresa irá te dar: ").split()
    salario = int(salario)

    if salario <= 3960:
        aumento = salario * 0.50
    
    elif salario <= 13200:
        aumento = salario * 0.20
    
    elif salario <= 26400:
        aumento = salario * 0.15
    
    else:
        aumento = salario * 0.10

    novo_salario = salario + aumento
    print("{}, o seu salário passará a ser: {:.2f} dinheiros.".format(nome, novo_salario))
    
    sa += salario
    aum += aumento

total_au = aum - sa
print("O acréscimo total que essa empresa terá em sua folha de pagamento é: {:.2f} dinheiros".format(total_au))