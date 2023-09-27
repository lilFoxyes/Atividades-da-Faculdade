

 
bonus_masculino_mais_15_anos = 0.05
bonus_feminino_mais_10_anos = 0.07
bonus_padrao = 500.00


dados_funcionarios = []


impacto_orcamento_total = 0.0


for i in range(100):
    nome_funcionario, sexo_funcionario, tempo_casa_funcionario, salario_mensal_funcionario = input("Digite o nome, sexo, tempo de casa (anos) e salário mensal do funcionário {}: ".format(i + 1)).split()
    salario_mensal_funcionario = float(salario_mensal_funcionario)
    tempo_casa_funcionario = int(tempo_casa_funcionario)
    dados_funcionarios.append((nome_funcionario, sexo_funcionario, tempo_casa_funcionario, salario_mensal_funcionario))


for nome_funcionario, sexo_funcionario, tempo_casa_funcionario, salario_mensal_funcionario in dados_funcionarios:
    if sexo_funcionario == "masculino" and tempo_casa_funcionario > 15:
        bonus_natal_funcionario = salario_mensal_funcionario * bonus_masculino_mais_15_anos
    elif sexo_funcionario == "feminino" and tempo_casa_funcionario > 10:
        bonus_natal_funcionario = salario_mensal_funcionario * bonus_feminino_mais_10_anos
    else:
        bonus_natal_funcionario = bonus_padrao
    
    impacto_orcamento_total += bonus_natal_funcionario
    print("{} recebe um Bônus de Natal de R$ {:.2f}".format(nome_funcionario, bonus_natal_funcionario))

print("O impacto total no orçamento da empresa devido ao Bônus de Natal é de R$ {:.2f}".format(impacto_orcamento_total))