

a, b, c = input("Digite 2 números e um caracter de operação aritmética (nessa ordem): ").split()

if a.isdigit() and b.isdigit():
    a = int(a)
    b = int(b)
    
    if c == "+":
        trem = a + b
        print("O resultado é: {}".format(trem))

    elif c == "-":
        trem = a - b
        print("O resultado é: {}".format(trem))

    elif c == "*":
        trem = a * b
        print("O resultado é: {}".format(trem))

    elif c == "/":
        if b == 0 and c =="/":
            print("Não se pode realizar divisão por zero, bobinho :P")
        else:
            trem = a / b
            print("O resultado é: {}".format(trem))

else:
    print("Não é hoje que vc vai conseguir quebrar o meu código!(Favor, ouça o son do riso do coringa)")


