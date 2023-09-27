
populacao_brasil = 211e6  
populacao_eua = 331e6  
ano = 2023  


while populacao_brasil <= populacao_eua:
    populacao_brasil *= 1.04  
    populacao_eua *= 1.02  
    ano += 1


print("No ano {}, a população brasileira supera a população americana.".format(ano))