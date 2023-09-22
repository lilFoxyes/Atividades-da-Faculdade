media_custo = 0
media_venda = 0
contador1 = 0
contador2 = 0

for i in range(5):
    x= int(input("Digite o custo de produção e direi se houve lucro ou prejuízo: "))
    y= int(input("Digite o valor da venda e direi se houve lucro ou prejuízo: "))
    
    if x > y:
        print("O prejuízo foi de: {}".format(int(x) - int(y)))
        contador1 +=1
    elif y > x:
        print("O lucro foi de: {}". format(int(y) - int(x)))
        contador2 += 1
    else:
        print("Não houve lucro ou prejuízo")
    media_custo += int(x)
    media_venda += int(y) 

media1 = media_custo/5
media2 = media_venda/5
print("A média do custo de produção é: {} e a média do valor da venda é: {}. Você teve prejuízo {}x e lucrou {}x com essas vendas". format(media1, media2, contador1, contador2))
