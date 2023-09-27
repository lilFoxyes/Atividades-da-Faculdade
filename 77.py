classes_de_iluminacao = {
    "quarto": 15,
    "sala de tv": 15,
    "salas": 18,
    "cozinha": 18,
    "varandas": 18,
    "escritório": 20,
    "banheiro": 20
}


total_lampadas = 0
total_potencia = 0


comodos_processados = []

while True:
    comodo = input("Nome do cômodo (ou 'vazio' para encerrar): ").lower()
    
    if comodo == 'vazio':
        break
    
    if comodo not in classes_de_iluminacao:
        print("Classe de iluminação inválida. Por favor, escolha entre os cômodos listados.")
        continue
    
    dimensao1 = float(input("Primeira dimensão do cômodo (metros): "))
    dimensao2 = float(input("Segunda dimensão do cômodo (metros): "))
    
    area_comodo = dimensao1 * dimensao2
    potencia_iluminacao = classes_de_iluminacao[comodo]
    num_lampadas = int(area_comodo * potencia_iluminacao / 60)
    
    comodo_processado = {
        'Nome do cômodo': comodo,
        'Área do cômodo': area_comodo,
        'Potência de iluminação': potencia_iluminacao,
        'Número de lâmpadas necessárias': num_lampadas
    }
    
    comodos_processados.append(comodo_processado)
    
    total_lampadas += num_lampadas
    total_potencia += num_lampadas * 60


for comodo in comodos_processados:
    print("Cômodo: {}".format(comodo['Nome do cômodo']))
    print("Área do Cômodo: {:.2f} metros quadrados".format(comodo['Área do cômodo']))
    print("Potência de Iluminação: {}W/m²".format(comodo['Potência de iluminação']))
    print("Número de Lâmpadas Necessárias: {}".format(comodo['Número de lâmpadas necessárias']))
    print()


print("Total de Lâmpadas para a Residência: {}".format(total_lampadas))
print("Total de Potência para a Residência: {}W".format(total_potencia))