

a, b, c = input("Digite 3 números e veremos se é um triângulo: ").split()
a = int(a)
b = int(b)
c = int(c)

if a + b > c or a + c > b or b + c > a:

    
    if a == b == c:
        print("É um triângulo equilátero")

    elif a == b != c or a != b == c or a == c != b:
        print("É um triângo isósceles")

    elif a != b != c:
        print("É um triângulo escaleno")

else:
    print("Isso nem é um triângulo, favor melhorar nos conceitos")


