temperatura_minima = 40  
temperatura_maxima = 15  


soma_temperaturas = 0
quantidade_dias = 0


for dia in range(1, 122):
    temperatura = float(input("Digite a temperatura do dia {}: ".format(dia)))
    

    if temperatura < temperatura_minima:
        temperatura_minima = temperatura
    
    
    if temperatura > temperatura_maxima:
        temperatura_maxima = temperatura
    
   
    soma_temperaturas += temperatura
    quantidade_dias += 1


temperatura_media = soma_temperaturas / quantidade_dias


dias_inferiores_a_media = 0


for dia in range(1, 122):
    temperatura = float(input("Digite a temperatura do dia {}: ".format(dia)))
    if temperatura < temperatura_media:
        dias_inferiores_a_media += 1


print("Menor temperatura: {:.2f}".format(temperatura_minima))
print("Maior temperatura: {:.2f}".format(temperatura_maxima))
print("Temperatura média: {:.2f}".format(temperatura_media))
print("Dias com temperatura inferior à média: {:.0f}".format(dias_inferiores_a_media))