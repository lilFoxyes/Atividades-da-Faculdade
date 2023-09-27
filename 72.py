total_bois = 90
bois = []

for i in range(total_bois):
    numero, peso = input("Digite o número de identificação e o peso do boi (separados por espaço): ").split()
    peso = float(peso)
    bois.append((numero, peso))

boi_mais_gordo = max(bois, key=lambda x: x[1])
boi_mais_magro = min(bois, key=lambda x: x[1])

print("Boi mais gordo - Número de Identificação: {}, Peso: {:.2f}".format(boi_mais_gordo[0], boi_mais_gordo[1]))
print("Boi mais magro - Número de Identificação: {}, Peso: {:.2f}".format(boi_mais_magro[0], boi_mais_magro[1]))