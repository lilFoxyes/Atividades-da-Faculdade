def ordenar_vetor_crescente(vetor):
    tamanho = len(vetor)
    
    for i in range(tamanho):
        for j in range(0, tamanho - i - 1):
            if vetor[j] > vetor[j + 1]:
                vetor[j], vetor[j + 1] = vetor[j + 1], vetor[j]

def obter_vetor():
    try:
        tamanho = int(input("Digite o tamanho do vetor: "))
        vetor = []
        for i in range(tamanho):
            elemento = int(input("Digite o elemento {}: ".format(i + 1)))
            vetor.append(elemento)
        return vetor
    except ValueError:
        print("Entrada inválida. Certifique-se de inserir números inteiros.")

print("Ordenação de Vetor usando o Método da Bolha")
vetor = obter_vetor()
if vetor:
    ordenar_vetor_crescente(vetor)
    print("Vetor ordenado em ordem crescente: {}".format(vetor))
