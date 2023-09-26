
x = float(input("Digite o trem de poluição aqui: "))

if 0.25 > x >= 0.05:
    print("Tudo normal no morro")

elif 0.30 > x >= 0.25:
    print("N tá tão bacana assim n~çao, se pá é alerta")

elif 0.40 > x >= 30:
    print("Industria A, favor parar de funcionar")

elif 0.50 > x >= 40:
    print("Xiiiiiiiiiii, tá começando a azerdar, industria B, favor parar as operações aí")

else:
    print("Já acabaram com o meio ambiente, agora vão ter que parar de funcionar, pode ir fechando as portas você também, industria C")