num_candidatos_femininos = 0
num_candidatos_masculinos = 0
idade_media_homens_com_experiencia = 0
porcentagem_homens_acima_45 = 0
num_mulheres_abaixo_35_com_experiencia = 0
menor_idade_mulher_com_experiencia = float("inf")


while True:
    numero_inscricao = int(input("Número de inscrição do candidato (ou 0 para encerrar): "))
    
    if numero_inscricao == 0:
        break
    
    idade = int(input("Idade do candidato: "))
    sexo = input("Sexo do candidato (masculino ou feminino): ").lower()
    experiencia = input("Experiência no serviço (sim ou não): ").lower()
    
    if sexo == "feminino":
        num_candidatos_femininos += 1
    elif sexo == "masculino":
        num_candidatos_masculinos += 1

    if sexo == "masculino" and experiencia == "sim":
        idade_media_homens_com_experiencia += idade

    if sexo == "masculino" and idade > 45:
        porcentagem_homens_acima_45 += 1

    if sexo == "feminino" and idade < 35 and experiencia == "sim":
        num_mulheres_abaixo_35_com_experiencia += 1

    if sexo == "feminino" and experiencia == "sim" and idade < menor_idade_mulher_com_experiencia:
        menor_idade_mulher_com_experiencia = idade


if num_candidatos_masculinos > 0:
    idade_media_homens_com_experiencia /= num_candidatos_masculinos
    porcentagem_homens_acima_45 = (porcentagem_homens_acima_45 / num_candidatos_masculinos) * 100


print("Número de candidatos do sexo feminino:", num_candidatos_femininos)
print("Número de candidatos do sexo masculino:", num_candidatos_masculinos)
print("Idade média dos homens com experiência no serviço:", idade_media_homens_com_experiencia)
print("Porcentagem de homens com mais de 45 anos entre o total de homens:", porcentagem_homens_acima_45, "%")
print("Número de mulheres com menos de 35 anos e com experiência no serviço:", num_mulheres_abaixo_35_com_experiencia)
print("Menor idade entre mulheres com experiência no serviço:", menor_idade_mulher_com_experiencia)