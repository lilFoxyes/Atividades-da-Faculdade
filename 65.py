associados = 3550
mensalidades = []


for i in range(associados):
    mensalidade = float(input("Digite o valor da mensalidade do associado {}: R$ ".format(i + 1)))
    mensalidades.append(mensalidade)


acumulado_reajustes = 0

for i, mensalidade in enumerate(mensalidades, 1):
    reajuste = mensalidade * 0.10
    mensalidade_reajustada = mensalidade + reajuste
    acumulado_reajustes += reajuste

    print("Associado {}: Mensalidade Atual: R$ {:.2f} - Reajuste: R$ {:.2f} - Mensalidade Reajustada: R$ {:.2f}".format(i, mensalidade, reajuste, mensalidade_reajustada))

print("Total acumulado dos reajustes: R$ {:.2f}".format(acumulado_reajustes))