total_homens_menores_idade = 0
total_homens_baixa_estatura = 0
total_mulheres_maiores_idade_alta_estatura = 0
total_pessoas_baixa_estatura = 0
total_pessoas_alta_estatura = 0


for i in range(10):
    nome, idade, sexo, altura = input("Digite o nome, idade, sexo (M/F) e altura (em metros): ").split()
    idade = int(idade)
    altura = float(altura)

    
    if idade < 21:
        
        if sexo == 'M':
            total_homens_menores_idade += 1
        
        if altura < 1.60:
            total_homens_baixa_estatura += 1
    
    elif idade >= 21 and sexo == 'M' and altura < 1.60:
        total_homens_baixa_estatura += 1
    
    elif idade >= 21 and sexo == 'F' and altura > 1.70:
        total_mulheres_maiores_idade_alta_estatura += 1

    if altura < 1.55:
        total_pessoas_baixa_estatura += 1
    
    elif altura > 1.70:
        total_pessoas_alta_estatura += 1


porcentagem_alta_estatura = (total_pessoas_alta_estatura / 1000) * 100


print("Total de homens menores de idade: {}".format(total_homens_menores_idade))
print("Total de homens de baixa estatura: {}".format(total_homens_baixa_estatura))
print("Total de mulheres maiores de idade e de alta estatura: {}".format(total_mulheres_maiores_idade_alta_estatura))
print("Total de pessoas de baixa estatura: {}".format(total_pessoas_baixa_estatura))
print("Porcentagem de pessoas de alta estatura: {:.2f}%".format(porcentagem_alta_estatura))