salario = 1320
sal = 0
tab_salario = []
cont_pobre = 0
cont_rico = 0

resposta = input("Gostaria de começar o cálculo da folha de pagamento desse mês? ")
if resposta == "Sim":
    while True:
    

        if resposta == "Sim":
            sal = int(input("Digite o salário do funcionário: "))
            tab_salario.append(sal)
            resposta2 = input("Gostaria de continuar? ")
                            
            if resposta2 == "Não":
                break    
              

        elif resposta == "Não":
            break

else:
    print("Digite algum trem válido aí fazendo favor.")


for sal in tab_salario:
    if salario * 5 > sal:
        cont_pobre += 1

    elif sal > salario * 10:
        cont_rico += 1

total = sum(tab_salario)

print("O total de pessoas que recebe menos de 5 salários mínimos é: {} \n  O total de pessoas que recebem mais do que 10 salários mínimos é: {} \n  O total gasto na folha de pagamento é: {}".format(cont_pobre, cont_rico, total))