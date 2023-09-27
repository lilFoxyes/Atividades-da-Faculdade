x = int(input("Digite a primeira nota para que eu posa calcular a sua média: "))
y = int(input("Digite a segunda nota: "))
z = int(input("Digite a terceira nota: "))

media = (x+y+z)/3

if 10 >= media >= 7:
    print("Parabéns, a sua média é {} e você está aprovado!".format(media))
elif 6.9 >= media >= 5.1:
    print("Infelizmente a sua média é {} e você está de recuperação!".format(media))
elif 5 >= media >= 0:
    print("Infelizmente a sua média é {} e você está reprovado!".format(media))
else:
    print("Não é possível obter essa média, por favor, insira números válidos")            