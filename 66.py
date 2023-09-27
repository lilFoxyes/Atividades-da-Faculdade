
REAJUSTE_ATE_2000 = 0.10
REAJUSTE_2000_5000 = 0.07
REAJUSTE_ACIMA_5000 = 0.03


salarios = []


for i in range(1000):
    salario = float(input("Digite o salário do funcionário {}: R$ ".format(i + 1)))
    salarios.append(salario)


for i, salario in enumerate(salarios, 1):
    if salario <= 2000:
        novo_salario = salario * (1 + REAJUSTE_ATE_2000)
    
    elif 2000 < salario <= 5000:
        novo_salario = salario * (1 + REAJUSTE_2000_5000)
    
    else:
        novo_salario = salario * (1 + REAJUSTE_ACIMA_5000)
    
    print("Funcionário {}: Salário antigo: R$ {:.2f} - Novo salário: R$ {:.2f}".format(i, salario, novo_salario))