n1 = 12
n2 = 17
n3 = 25


a = int(input("Digite o seu nível de professor na escola: "))

if a == 1:
    h = int(input("Digite a quantidade de horas trabalhadas nesse mês: "))
    salario = n1 * h
    print("O salário desse mês é: {} dinheiros.".format(salario))

elif a == 2:
    h = int(input("Digite a quantidade de horas trabalhadas nesse mês: "))
    salario = n2 * h
    print("O salário desse mês é: {} dinheiros.".format(salario))

elif a == 3:
    h = int(input("Digite a quantidade de horas trabalhadas nesse mês: "))
    salario = n3 * h
    print("O salário desse mês é: {} dinheiros.".format(salario))

else:
    print("Já tá inventando nível, favor digitar o trem certinho.")


