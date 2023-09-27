vetor = []


n = int(input("Digite a quantidade de números a serem lidos: "))


for i in range(n):
    numero = int(input("Digite o {}º número: ".format(i + 1)))
    if numero % 4 == 0:
        vetor.append(numero)


if len(vetor) > 50:
    vetor = vetor[:50]


print("Vetor com números divisíveis por 4:", vetor)