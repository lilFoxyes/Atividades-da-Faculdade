
lista1 = [0.0] * 25
lista2 = [0.0] * 25


for i in range(25):
    lista1[i] = float(input("Digite o {}º elemento da primeira lista: ".format(i + 1)))
    lista2[i] = float(input("Digite o {}º elemento da segunda lista: ".format(i + 1)))

lista_resultante = [0.0] * 50


for i in range(25):
    lista_resultante[i * 2] = lista1[i]
    lista_resultante[i * 2 + 1] = lista2[i]

print("Lista resultante intercalada:")
print(lista_resultante)