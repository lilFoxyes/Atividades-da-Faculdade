
idade = int(input("Digite a sua idade: "))

if 7 >= idade >= 5:
    print("Infantil A")

elif 10 >= idade >= 8:
    print("Infantil B")

elif 13 >= idade >= 11:
    print("Juvenil A")

elif 17 >= idade >= 14:
    print("Juvenil B")

elif 25 >= idade >= 18:
    print("Sênior")

else:
    print("Fora da faixa etária")
