placas = [0] * 10

for i in range(10):
    placa = input("Digite aqui a placa do carro: ")
    final = int(placa) % 10
    placas[final] += 1

for final, placas in enumerate(placas):
    print("Placas com o final {}: {}".format(final, placas))

