dados = []
soma_nota = 0
for i in range(5):
    nome, matricula, nota = input("Digite o seu nome, a sua matrícula e a sua nota: ").split()
    nota = int(nota)
    dados.append((nome, matricula, nota))

aprovados = [(nome, matricula, nota) for nome, matricula, nota in dados if nota >= 7]
reprovados = [(nome, matricula, nota) for nome, matricula, nota in dados if 7 > nota]

for aluno in dados:
    soma_nota += aluno[2]

media_nota = soma_nota / len(dados)

print("A média da turma é: {:.2f} \n Os alunos que foram reprovados são: {} \n Os que foram aprovados são: {} ".format(media_nota, reprovados, aprovados))