
seg = int(input("Digite uma quantidade de segundos e te direi quantos minutos e horas são: "))

min = seg // 60
h = seg // 3600
seg_sobra = seg % 60

if min >= 60:
    min = min % 60    

print("{} segundos são: {} horas, {} minutos e {} segundos".format(seg, h, min, seg_sobra))
