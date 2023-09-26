tamanhos = []
pp = 0
p = 0
m = 0
g = 0
gg = 0
roupas = 0
for i in range(10):
    tamanho = input("Digite o tamanho da roupa (PP, P, M, G e GG): ")
    tamanhos.append(tamanho)
    roupas += 1

for tamanho in tamanhos:
    if tamanho == "PP":
            pp += 1

    elif tamanho == "P":
            p += 1     

    elif tamanho == "M":
            m += 1

    elif tamanho == "G":
            g += 1

    elif tamanho == "GG":
            gg +=1           

         

        

porc_pp = (pp / roupas) * 100
porc_p = (p / roupas) * 100
porc_m = (m / roupas) * 100
porc_g = (g / roupas) * 100
porc_gg = (gg / roupas) * 100

print("A quantidade de roupas é: {} \n A porcentagem de PP é: {:.2f}% \n A porcentagem de P é: {:.2f}% \n A porcentagem de M é: {:.2f}% \n A porcentagem de G é: {:.2f}% \n A porcentagem de GG é: {:.2f}% \n ".format(roupas, porc_pp, porc_p, porc_m, porc_g, porc_gg))