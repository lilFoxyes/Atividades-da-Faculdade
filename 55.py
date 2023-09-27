
homem_mais_velho = {"nome": None, "idade": 0}
mulher_mais_velha = {"nome": None, "idade": 0}


total_mulheres = 0


mulheres_verdes_louros_18_35 = 0

while True:
    
    entrada = input("Digite o nome, sexo, cor dos olhos, cor dos cabelos e idade da pessoa: ")
    dados = entrada.split()

    nome = dados[0]
    sexo = dados[1].upper()
    olhos = dados[2].lower()
    cabelos = dados[3].lower()
    idade = int(dados[4])

    
    if sexo == "M" and idade > homem_mais_velho["idade"]:
        homem_mais_velho["nome"] = nome
        homem_mais_velho["idade"] = idade
    elif sexo == "F" and idade > mulher_mais_velha["idade"]:
        mulher_mais_velha["nome"] = nome
        mulher_mais_velha["idade"] = idade

    
    if sexo == "F":
        total_mulheres += 1
        if 18 <= idade <= 35 and olhos == "verdes" and cabelos == "louros":
            mulheres_verdes_louros_18_35 += 1

    
    continuar = input("Deseja continuar com o cadastro de pesquisa? (S para Sim, qualquer outra tecla para encerrar): ").upper()
    if continuar != "S":
        break


if total_mulheres > 0:
    porcentagem = (mulheres_verdes_louros_18_35 / total_mulheres) * 100
else:
    porcentagem = 0


print("O homem mais velho é: {} com {} anos.".format(homem_mais_velho["nome"], homem_mais_velho["idade"]))
print("A mulher mais velha é: {} com {} anos.".format(mulher_mais_velha["nome"], mulher_mais_velha["idade"]))
print("A porcentagem de mulheres com olhos verdes, cabelos louros e idade entre 18 e 35 anos é: {:.2f}%.".format(porcentagem))
