
total_contas = 0
total_pagamento = 0





while True:
    codigo_praga = input("Digite o código da praga (A, B, C ou D) ou 'fim' para encerrar: ").lower()
    
    if codigo_praga == "fim":
        break  
    
    area_pulverizada = float(input("Digite a área pulverizada em acres: "))
    
   
    if codigo_praga == "a":
        preco_por_acre = 10.00
    elif codigo_praga == "b":
        preco_por_acre = 20.00
    elif codigo_praga == "c":
        preco_por_acre = 30.00
    elif codigo_praga == "d":
        preco_por_acre = 25.00
    
    custo_pulverizacao = area_pulverizada * preco_por_acre
    
    
    if area_pulverizada > 1000:
        custo_pulverizacao *= 0.95  
    
    if custo_pulverizacao > 25000.00:
        custo_pulverizacao *= 0.90  
    
    total_contas += 1
    total_pagamento += custo_pulverizacao
    
   
    print("{:<10} {:<15} R$ {:<.2f}".format(total_contas, codigo_praga.upper(), custo_pulverizacao))


print("\nTotal de contas: {}".format(total_contas))
print("Total de pagamento: R$ {:.2f}".format(total_pagamento))
