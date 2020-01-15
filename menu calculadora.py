import soma_subtração_multiplicação_divisao

menu = int(input('Quais opções você quer'
                 '\n[1] soma'
                 '\n[2] subtração'))

if menu == 1:
    soma_subtração_multiplicação_divisao.soma()
elif menu == 2:
    soma_subtração_multiplicação_divisao.subtracao()
