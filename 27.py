dia, mes, ano = input("Digite (com espaços) o dia, mês e ano. Eu te falarei se é uma data válida: ").split()

dia = int(dia)
mes = int(mes)
ano = int(ano)


if 12 >= mes >= 1:

        if mes in [1, 3, 5, 7, 8, 10, 12]:
            dias = 31

        elif mes in [4, 6, 11]:
            dias = 30

        elif mes in [2]:
            if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0):
                dias = 29

            else:
                dias = 28    

        if dias >= dia >= 1:
            print("{}/{}/{}, o seu ano é válido!".format(dia, mes, ano))
        else:
            print("Data inválida")               
else:
    print("Data inválida")
