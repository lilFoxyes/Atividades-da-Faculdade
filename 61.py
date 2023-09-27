

numero1, numero2 = input("Digite dois números inteiros separados por espaço: ").split()
numero1 = int(numero1)
numero2 = int(numero2)


soma_multiplos_5 = 0
contagem_multiplos_5 = 0

for numero in range(numero1 + 1, numero2):
    if numero % 5 == 0:
        soma_multiplos_5 += numero
        contagem_multiplos_5 += 1

if contagem_multiplos_5 > 0:
    media_multiplos_5 = soma_multiplos_5 / contagem_multiplos_5
    print("A média dos múltiplos de 5 entre {} e {} é: {:.2f}".format(numero1, numero2, media_multiplos_5))
else:
    print("Não existem múltiplos de 5 entre {} e {}.".format(numero1, numero2))