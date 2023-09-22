contador1 = 0
contador2 = 0
for i in range(5):
    nome, sexo = input("Digite o seu nome e a sua idade: ").split()
    if sexo == "feminino":
        contador1 = contador1 + 1
    elif sexo == "masculino":
        contador2 = contador2 + 1    

print("O número de mulheres é: {} e de homens é: {}".format(contador1, contador2))