posi = 0
for i in range (5):
    x = int(input("Digite um número: "))
    
    if x > 0:
        print("{} é positivo".format(x))
        
    elif 0 > x :
        print("{} é negativo".format(x)) 
        
    else:
        print("Zero!")
    posi += x    

media_posi = posi/5

print("A média dos números positivos é {}".format(media_posi))

