nota = []
contador = 0


for i in range(5):
    notas = int(input("Digite as notas dos alunos dessa turma: "))    
    nota.append(notas)
    media = sum(nota) / len(nota)
    if notas < media:
        contador += 1

   

print("A média da turma é: {} e a quantidade de alunos que ficou abaixo da média é: {}".format(media, contador))        
