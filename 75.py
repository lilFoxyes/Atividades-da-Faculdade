
preco_kwh = float(input("Digite o preço do kWh consumido: "))
maior_consumo = menor_consumo = total_residencial = total_comercial = total_industrial = total_consumo = 0
quantidade_consumidores = 0

consumidores = []

while True:
    numero_consumidor = int(input("Digite o número do consumidor (ou 0 para encerrar): "))
    if numero_consumidor == 0:
        break

    consumo_kwh = float(input("Digite a quantidade de kWh consumidos: "))
    tipo_consumidor = input("Digite o código do tipo de consumidor (residencial, comercial, industrial): ").lower()

    total_a_pagar = preco_kwh * consumo_kwh


    if tipo_consumidor == "residencial":
        total_residencial += total_a_pagar
    elif tipo_consumidor == "comercial":
        total_comercial += total_a_pagar
    elif tipo_consumidor == "industrial":
        total_industrial += total_a_pagar

    
    if consumo_kwh > maior_consumo:
        maior_consumo = consumo_kwh
    if consumo_kwh < menor_consumo or quantidade_consumidores == 0:
        menor_consumo = consumo_kwh


    total_consumo += consumo_kwh
    quantidade_consumidores += 1


    consumidores.append((numero_consumidor, total_a_pagar))


media_geral = total_consumo / quantidade_consumidores


print("Consumidores processados:", quantidade_consumidores)
print("Maior consumo:", maior_consumo)
print("Menor consumo:", menor_consumo)
print("Total de consumo residencial:", total_residencial)
print("Total de consumo comercial:", total_comercial)
print("Total de consumo industrial:", total_industrial)
print("Média geral de consumo:", media_geral)


for numero, total in consumidores:
    print("Consumidor:", numero)
    print("Total a pagar:", total)