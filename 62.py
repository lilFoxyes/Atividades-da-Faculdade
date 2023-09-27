
gabarito = "ABB"
respostas_estudantes = []

for i in range(30):
    respostas = input("Digite as respostas do estudante {} (por exemplo, 'ABC'): ".format(i + 1))
    respostas_estudantes.append(respostas)

for i, respostas in enumerate(respostas_estudantes, 1):
    num_questoes_corretas = sum(1 for a, b in zip(gabarito, respostas) if a == b)

    if num_questoes_corretas == 0:
        print("Estudante {}: Eliminado".format(i))
    else:
        questoes_corretas = [j + 1 for j, (a, b) in enumerate(zip(gabarito, respostas)) if a == b]
        print("Estudante {}: Gabarito {}".format(i, ', '.join(map(str, questoes_corretas))))

print("Gabarito: {}".format(gabarito))