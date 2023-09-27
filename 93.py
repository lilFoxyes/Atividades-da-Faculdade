matriz_a = []


for i in range(12):
    elemento = int(input("Digite o elemento {}: ".format(i + 1)))
    matriz_a.append(elemento)


matriz_b = []


for elemento in matriz_a:
    if elemento % 2 == 1:  # Verifica se o elemento é ímpar
        matriz_b.append(elemento * 2)  # Multiplica por 2 e adiciona a B
    else:
        matriz_b.append(elemento)  # Mantém o elemento igual e adiciona a B


print("Matriz B (Aplicando a regra):")
for elemento in matriz_b:
    print(elemento)