canais = {"4": 0, "5": 0, "7": 0, "12": 0}
total_pessoas = 0

while True:
    canal, pessoas = input("Digite o número do canal e o número de pessoas assistindo (ou 0 para encerrar): ").split()
    canal = canal.lower()  # Converter para minúsculas para garantir que seja insensível a maiúsculas e minúsculas
    pessoas = int(pessoas)

    if canal == "0":
        break
    
    canais[canal] += pessoas
    total_pessoas += pessoas

for canal, audiencia in canais.items():
    porcentagem = (audiencia / total_pessoas) * 100
    print("Canal {}: {:.2f}% de audiência".format(canal, porcentagem))