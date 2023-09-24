
nome, mat, lab, sem, ex = input("Digite o seu nome, a matrícula, a sua nota do Lab, da Avaliação e do Exame: ").split()

lab = float(lab)
sem = float(sem)
ex = float(ex)
mat = int(mat)

if 10 >= lab >=0 and 10 >= sem >= 0 and 10 >= ex >= 0:
    nota = (lab * 2 + sem * 3 + ex * 5) / 10
    
    if 10 >= nota >= 8:
        rank = "A"
    
    elif 7.9 >= nota >= 7:
        rank = "B"

    elif 6.9 >= nota >= 6:
        rank = "C"

    elif 5.9 >= nota >= 5:
        rank = "D"

    else:
        rank = "R"    


else:
    print("Não tenta brincar com o meu código n, bota um número válido aí fazendo favor :D.")
        
print("{} com a matrícula nº {}, a sua nota foi: {:.2f}, portanto está na classificação {}".format(nome, mat, nota, rank))

