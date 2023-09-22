x = int(input("Digite um número: "))
y = int(input("Digite outro número: "))

if x > y:
    print("{} é maior do que {}".format(x, y))
elif x < y:
    print("{} é maior do que {}".format(y, x))
else:
    print("Os números são iguais")        