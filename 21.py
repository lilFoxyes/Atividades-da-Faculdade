

a, b, c = input("Digite 3 números e irei colocá-los em ordem crescente: ").split()

a = int(a)
b = int(b)
c = int(c) 

maior = max(a, b, c)
menor = min(a, b, c)
meio = a+b+c
meio_def = meio - maior - menor

print("O maior número é o {}, o segundo maior é o {} e o menor é {}".format(maior, meio_def, menor))