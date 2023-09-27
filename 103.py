numero_de_voos = 37
lugares_disponiveis_por_voo = [100] * numero_de_voos
reservas_bem_sucedidas = []
identidade_cliente = 0

while True:
    entrada = input("Digite o número da identidade do cliente e o número do voo desejado (separados por espaço): ")
    identidade_cliente, numero_voo_desejado = map(int, entrada.split())
    
    if identidade_cliente == 99999:
        break

    if numero_voo_desejado >= 1 and numero_voo_desejado <= numero_de_voos:
        voo_index = numero_voo_desejado - 1
        
        if lugares_disponiveis_por_voo[voo_index] > 0:
            reservas_bem_sucedidas.append((identidade_cliente, numero_voo_desejado))
            lugares_disponiveis_por_voo[voo_index] -= 1
        else:
            print("Desculpe, não há lugares disponíveis no voo {}.".format(numero_voo_desejado))
    else:
        print("Voo inválido. Por favor, escolha um número de voo entre 1 e {}.".format(numero_de_voos))

print("Pedidos de reserva bem-sucedidos:")
for reserva in reservas_bem_sucedidas:
    identidade_cliente, numero_voo_desejado = reserva
    print("Identidade do cliente: {}, Número do voo: {}".format(identidade_cliente, numero_voo_desejado))