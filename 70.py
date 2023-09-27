idades = []
idade = int(input("Digite a idade do indivíduo (ou 0 para encerrar): "))

while idade != 0:
    idades.append(idade)
    idade = int(input("Digite a idade do indivíduo (ou 0 para encerrar): "))

if len(idades) > 0:
    idade_media = sum(idades) / len(idades)
    print("A idade média deste grupo de indivíduos é: {:.2f}".format(idade_media))
else:
    print("Nenhum dado foi inserido para calcular a idade média.")