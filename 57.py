
matriculas = []
medias_finais = []
frequencias = []
soma_medias = 0
total_alunos_reprovados = 0
total_alunos_abaixo_media_turma = 0

for i in range(10):
    
    matricula, nota1, nota2, nota3, frequencia = input("Digite a matrícula, 3 notas e a frequência do aluno (separados por espaço): ").split()
    
    matriculas.append(matricula)
    nota1 = float(nota1)
    nota2 = float(nota2)
    nota3 = float(nota3)
    frequencia = int(frequencia)
    media_final = (nota1 + nota2 + nota3) / 3
    medias_finais.append(media_final)
  
    frequencias.append(frequencia)
    soma_medias += media_final
    
    if media_final < 6 or frequencia < 40:
        total_alunos_reprovados += 1
    
    if media_final < 6:
        total_alunos_abaixo_media_turma += 1

media_turma = soma_medias / len(matriculas)

maior_media_final = max(medias_finais)
menor_media_final = min(medias_finais)

for i in range(10):
    print("Matrícula: {}, Média Final: {:.2f}".format(matriculas[i], medias_finais[i]))

print("Maior Média Final da Turma: {:.2f}".format(maior_media_final))
print("Menor Média Final da Turma: {:.2f}".format(menor_media_final))
print("Média da Turma: {:.2f}".format(media_turma))
print("Total de Alunos Reprovados: {}".format(total_alunos_reprovados))
print("Total de Alunos Abaixo da Média da Turma: {}".format(total_alunos_abaixo_media_turma))