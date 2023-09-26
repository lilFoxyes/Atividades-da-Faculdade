

nome, salario_fixo, inscri, tv42, tv20 = input("Digite o nome, salario, inscrição e quantidade de tv's 42(ou superior) e 20(ou inferior) (nessa ordem) vendidos: ").split()

salario_fixo = int(salario_fixo)
tv42 = int(tv42)
tv20 = int(tv20)

if 10 > tv42 >= 1:
    comi42 = tv42 * 50

elif tv42 >= 10:
    comi42 = tv42 * 100

else:
    comi42 = tv42 * 0

if 20 > tv20 >= 1:
    comi20 = tv20 * 20

elif tv20 >= 20:
    comi20 = tv20 * 40

else:
    comi20 = tv20 * 0

sa_inss = salario_fixo * 0.92
sa_comi = sa_inss + comi42 + comi20


if sa_comi >= 3000:
    sa_total = sa_comi * 0.95

else: 
    sa_total = sa_comi

print("{}, de inscrição {}, seu salário bruto é {:.2f} e o líquido é {:.2f}".format(nome, inscri, salario_fixo, sa_total))

