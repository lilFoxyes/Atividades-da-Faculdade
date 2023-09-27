despesas = {}


while True:
    linha = input("Digite a descrição da despesa e o valor (separados por espaço) ou 'Total' para encerrar: ")
    if linha == 'Total':
        break
    
    descricao, valor = linha.split()
    valor = float(valor)
    

    if descricao in despesas:
        despesas[descricao] += valor
    else:
        despesas[descricao] = valor


for descricao, valor in despesas.items():
    print("{} {:.2f}".format(descricao, valor))


total_despesas = sum(despesas.values())
print("Total {:.2f}".format(total_despesas))