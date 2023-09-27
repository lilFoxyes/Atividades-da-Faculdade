total_compras_vista = 0
total_compras_prazo = 0
total_pagamentos_efetuados = 0

while True:
    transacao = input("Insira o valor da transação e o código (* para compra à vista, + para compra a prazo, - para pagamento efetuado, ou 0 para sair): ")
    
    if transacao == '0':
        break

    valor, codigo = transacao.split()
    valor = float(valor)

    if codigo == '*':
        total_compras_vista += valor
    elif codigo == '+':
        total_compras_prazo += valor
    elif codigo == '-':
        total_pagamentos_efetuados += valor

print("Relatório de Transações:")
print("Total de Compras à Vista: R$ {:.2f}".format(total_compras_vista))
print("Total de Compras a Prazo: R$ {:.2f}".format(total_compras_prazo))
print("Total de Pagamentos Efetuados: R$ {:.2f}".format(total_pagamentos_efetuados))