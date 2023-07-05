import os

import share as sh
menu = """
Digite a seguinte letra para seguir:

[d] - Deposito
[s] - Saque
[e] - Estrato
[x] - Sair
"""
MSG_INPUT = 'Por Favor digite o valor: '

extrato = ""
LIMIT_DRAW_FOR_DAY = 500.0
AMOUT_DRAW_FOR_DAY = 3
account = 0
account_controller = 0


while True:
    v = input(menu).lower()

    if v == 'd':
        sh.clear()
        ui = sh.convert_value(input(MSG_INPUT))
        if ui <= 0:
            print('Erro - Valor precisa ser maior que 0.')
            continue
        account += ui
        extrato += f"Deposito = R$ {ui:.2f} \n"
        print('Operação feita com sucesso')
    elif v == 's':
        sh.clear()
        ui = sh.convert_value(input(MSG_INPUT))
        if ui <= 0:
            print('Erro - Valor precisa ser maior que 0.')
            continue
        if account_controller >= AMOUT_DRAW_FOR_DAY:
            print('Erro - Atingiu número maximo de saques por dia.')
            continue
        if ui > LIMIT_DRAW_FOR_DAY:
            print(f"Erro - Máximo por saque é R$ {LIMIT_DRAW_FOR_DAY:.2f}")
            continue
        if (account - ui) <= 0.0:
            print("Erro - Saldo negativo para esse valor.")
            continue
        account -= ui
        account_controller += 1
        extrato += f"Saque = R$ {ui:.2f}\n"
        print('Operação feita com sucesso')

    elif v == 'e':
        print(f'Saldo = R$ {account:.2f}')
        print(extrato)
    elif v == 'x':
        print('Saindo ...')
        break
    else:
        print('Erro Entrada invalida')

