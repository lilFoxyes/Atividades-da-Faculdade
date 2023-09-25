lista_numeros = []


primeiro, segundo = input("Digite 2 números e irei calcular os números pares entre eles: ").split()

primeiro = int(primeiro)
segundo = int(segundo)

for numero in range(primeiro, segundo + 1):
    if numero % 2 == 0:
        lista_numeros.append(numero)

numero_par = sum(lista_numeros)
quantidade = len(lista_numeros)

print("A quantidade de números pares entre {} e {} é: {} e a soma desses números é: {}".format(primeiro, segundo, quantidade, numero_par))