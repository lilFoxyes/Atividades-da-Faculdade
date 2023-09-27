

dia_mais_louco = 0  
maior_venda = 0


vendas_por_dia = []
for dia in range(1, 31):
    vendas = int(input("Quantos CD's foram vendidos no dia {} de abril? ".format(dia)))
    vendas_por_dia.append(vendas)


for dia, vendas in enumerate(vendas_por_dia, 1):
    if vendas > maior_venda:
        dia_mais_louco = dia
        maior_venda = vendas


print("No dia mais maluco de abril, dia {}, vendemos {} CD's!".format(dia_mais_louco, maior_venda))
print("No total, vendemos {} CD's durante o mês inteiro!".format(sum(vendas_por_dia)))