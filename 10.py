x = int(input("Digite um número: "))


if x > 80:
    print("{} é maior do que 80".format(x))
elif x < 25:
    print("{} é menor do que 25".format(x))
elif x == 40:
    print("{}".format(x))
else:
    print("É só um número comum")
