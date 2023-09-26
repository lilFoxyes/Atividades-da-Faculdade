

cpf, nome, renda_mensal, num_dependentes = input("Digite o número do CPF, nome do contribuinte, renda mensal e número de dependentes: ").split()

renda_mensal = float(renda_mensal)
num_dependentes = int(num_dependentes)

if len(cpf) == 11:
    desconto_dependentes = num_dependentes * 90

    if renda_mensal <= 287.27:
        inss = renda_mensal * 0.08
    elif renda_mensal <= 478.78:
        inss = renda_mensal * 0.09
    elif renda_mensal <= 957.56:
        inss = renda_mensal * 0.11
    else:
        inss = 105.33

    renda_liquida = renda_mensal - inss - desconto_dependentes

    if renda_liquida <= 900.00:
        aliquota = 0.0
        deducao = 0.0
    elif renda_liquida <= 1800.00:
        aliquota = 0.15
        deducao = 135.00
    else:
        aliquota = 0.25
        deducao = 315.00

    imposto_renda = (renda_liquida * aliquota) - deducao

    print("CPF: {}, Nome: {}, Renda Líquida: R$ {:.2f}, Imposto de Renda a pagar: R$ {:.2f}".format(cpf, nome, renda_liquida, imposto_renda))
else:
    print("Digite um CPF válido!")