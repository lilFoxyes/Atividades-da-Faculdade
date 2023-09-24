
from datetime import datetime


nascimento = input("Digite a sua data de nascimento (no formato DD/MM/AAAA): ")


nascimento = datetime.strptime(nascimento, "%d/%m/%Y")


hoje = datetime.now()


diferenca = hoje - nascimento


idade = diferenca.days // 365

print("A sua idade é: {} anos".format(idade))