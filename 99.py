def ler_vetor():
    vetor = []
    for i in range(6):
        valor = int(input("Digite o elemento {} do vetor: ".format(i + 1)))
        vetor.append(valor)
    return vetor

def ordenar_vetor_decrescente(vetor):
    n = len(vetor)
    
    for i in range(n - 1):
        
        indice_max = i
        for j in range(i + 1, n):
            if vetor[j] > vetor[indice_max]:
                indice_max = j
        
        
        vetor[i], vetor[indice_max] = vetor[indice_max], vetor[i]





vetor = ler_vetor()


ordenar_vetor_decrescente(vetor)


print("Vetor Ordenado em Ordem Decrescente:")
for elemento in vetor:
    print(elemento, end=" ")