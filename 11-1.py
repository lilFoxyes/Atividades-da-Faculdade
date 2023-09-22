import random 

contador = 0

x = 0

for i in range(80):
    x = random.randint(0, 999)
    print(x)
    if 10 <= x <= 150:
        contador = contador + 1

print("A quantidade de números aleatórios entre 10 e 150 é: {}".format(contador))        

