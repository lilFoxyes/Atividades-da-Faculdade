estoque = {}

def listar_estoque():
    print("Estoque atual:")
    for codigo, quantidade in estoque.items():
        print("Código: {}, Quantidade: {}".format(codigo, quantidade))

def processar_pedidos():
    while True:
        pedido = input("Digite o número do cliente, código da mercadoria e quantidade desejada (ou '0' para encerrar): ")
        if pedido == '0':
            break

        cliente, codigo, quantidade = pedido.split()
        quantidade = int(quantidade)

        if codigo in estoque:
            if estoque[codigo] >= quantidade:
                estoque[codigo] -= quantidade
                print("Pedido do cliente {} atendido. Mercadoria {} retirada do estoque.".format(cliente, codigo))
            else:
                print("Cliente {}: Não temos a mercadoria {} em estoque suficiente.".format(cliente, codigo))
        else:
            print("Cliente {}: Mercadoria {} não encontrada no estoque.".format(cliente, codigo))

def main():
    print("Bem-vindo ao sistema de atualização de estoque.")
    
    print("Digite o estoque inicial (ou '0' para encerrar):")
    while True:
        entrada = input("Digite o código da mercadoria e quantidade (ou '0' para encerrar): ")
        if entrada == '0':
            break

        codigo, quantidade = entrada.split()
        estoque[codigo] = int(quantidade)

    listar_estoque()

    processar_pedidos()

    listar_estoque()

if __name__ == "__main__":
    main()
