dados = []
soma_nota = 0
for i in range(5):
    nome, nota = input("Digite o seu nome e a sua nota: ").split()
    nota = int(nota)
    dados.append((nome, nota))

for aluno in dados:
    soma_nota += aluno[1]

media_nota = soma_nota / len(dados)



abaixo_media = [(nome, nota) for nome, nota in dados if media_nota > nota]



for nome, nota in abaixo_media:
    print("Os alunos que foram reprovados são: {}, {:.2f} ".format(nome, nota ))

print("A média da turma é: {:.2f}".format(media_nota))    