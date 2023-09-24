

for i in range(5):
    nome, idade, sexo, salario = input("Digite o seu nome, idade, sexo (m ou f) e salário e direi o seu abono acrescido no salário: ").split()
    idade = int(idade)
    salario = int(salario)
    
    if idade >= 30 and sexo == "m":
        abono = 100

    elif idade < 30 and sexo == "m":
        abono = 50

    elif idade >= 30 and sexo == "f":
        abono = 200

    elif idade < 30 and sexo == "f":
        abono = 80

    salario_total = salario + abono
    print("{} o seu abono será de: {} dinheiros, totalizando um salário de: {} dinheiros".format(nome, abono, salario_total))