
numero = int(input("Digite um número para calcular a fatorial: "))

def calcular_fatorial(N):
    fatorial = 1
    for i in range(1, N + 1):
        fatorial *= i
    return fatorial




resultado = calcular_fatorial(numero)


print("A fatorial de {} é igual a {}.".format(numero, resultado))