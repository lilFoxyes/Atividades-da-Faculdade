
lab, sem, ex = input("Digite a sua nota do Lab, da Avaliação e do Exame: ").split()

lab = float(lab)
sem = float(sem)
ex = float(ex)

if 10 >= lab >=0 and 10 >= sem >= 0 and 10 >= ex >= 0:
    nota = (lab * 2 + sem * 3 + ex * 5) / 10
    print(" A sua nota final é: {:.2f}".format(nota))

else:
    print("Não tenta brincar com o meu código n, bota um número válido aí fazendo favor :D.")
        


