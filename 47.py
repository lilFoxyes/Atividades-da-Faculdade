dados = []

for i in range(5):
    num = int(input("Digite um número: "))
    dados.append(num)

maior = max(dados)
menor = min(dados)
meio_lista = sorted(dados) 
meio = meio_lista[len(dados) // 2]

print("O maior é o número: {}".format(maior))
print("O do meio é o número: {}".format(meio))
print("O menor número é o: {}".format(menor))
