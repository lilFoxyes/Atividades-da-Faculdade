dados = []

for i in range(5):
    nome, idade = input("Digite o seu nome e a sua idade: ").split()
    idade = int(idade)
    dados.append((nome, idade))

idades = [idade for nome, idade in dados]
menor_idade = min(idades)
maior_idade = max(idades)
mais_novo = [(nome, idade) for nome, idade in dados if idade == menor_idade]
mais_velho = [(nome, idade) for nome, idade in dados if idade == maior_idade]


for nome, idade in mais_novo:
    print("O mais novo(a) dessa escola é o(a) {} e ele(a) tem {} anos".format(nome, idade))

for nome, idade in mais_velho:
    print("O mais velho(a) dessa escola é o(a) {} e ele(a) tem {} anos".format(nome, idade))

