
melhor_salario = 0
pior_salario = 0
matricula_melhor = ""
matricula_pior = ""
soma_salarios = 0
contador_servidores = 0


while True:
    matricula = input("Digite a matrícula do servidor (0 para sair): ")
    
    if matricula == "0":
        break
    
    salario = float(input("Digite o salário do servidor: "))
    
    
    if contador_servidores == 0:
        matricula_melhor = matricula
        matricula_pior = matricula
    
    
    soma_salarios += salario
    contador_servidores += 1
    
    
    if contador_servidores > 1:
        if salario > melhor_salario:
            melhor_salario = salario
            matricula_melhor = matricula
        if salario < pior_salario:
            pior_salario = salario
            matricula_pior = matricula
    

if contador_servidores > 0:
    
    media_salarios = soma_salarios / contador_servidores
    
    
    print("Matrícula e salário do servidor melhor remunerado:")
    print("Matrícula: {}, Salário: {:.2f}".format(matricula_melhor, melhor_salario))
    
    print("Matrícula e salário do servidor pior remunerado:")
    print("Matrícula: {}, Salário: {:.2f}".format(matricula_pior, pior_salario))
    
    print("Média dos salários pagos: {:.2f}".format(media_salarios))
else:
    print("Nenhum servidor foi inserido.")