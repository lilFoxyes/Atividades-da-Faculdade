
valor_taxa = int(input("Digite o valor da taxa em centavos: "))


selos_5_centavos = valor_taxa // 5
selos_3_centavos = (valor_taxa % 5) // 3
total_selos = selos_5_centavos + selos_3_centavos

print("Menor número de selos de 5 centavos:", selos_5_centavos)
print("Menor número de selos de 3 centavos:", selos_3_centavos)
print("Total de selos necessários:", total_selos)