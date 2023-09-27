gabarito = input("Digite o gabarito das 10 questões: ").split()


num_alunos = 0
notas = {}


aprovados = 0
maior_freq_nota = None
maior_freq = 0


while True:
    entrada = input("Digite o número do aluno e suas respostas (separados por espaço) ou 9999 para encerrar: ")
    if entrada == '9999':
        break
    
    num_aluno, *respostas = entrada.split()
    
   
    nota = sum([1 for i in range(10) if respostas[i] == gabarito[i]])
    
   
    notas[num_aluno] = nota
    
  
    if nota >= 6.0:
        aprovados += 1

  
    if nota in maior_freq_nota:
        maior_freq_nota[nota] += 1
    else:
        maior_freq_nota[nota] = 1

    num_alunos += 1


for nota, freq in maior_freq_nota.items():
    if freq > maior_freq:
        maior_freq = freq
        nota_maior_freq = nota


porcentagem_aprovacao = (aprovados / num_alunos) * 100 if num_alunos > 0 else 0


for aluno, nota in notas.items():
    print("Aluno: {} - Nota: {}".format(aluno, nota))

print("Porcentagem de Aprovação: {:.2f}%".format(porcentagem_aprovacao))
print("Nota com Maior Frequência: {}".format(nota_maior_freq))