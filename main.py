import share as sh
import bank
menu = """
Digite a seguinte letra para seguir:

[d] - Deposito
[s] - Saque
[e] - Estrato
[a] - Cadastrar Novo Usuario
[b] - Cadastrar Conta
[x] - Sair
"""
MSG_INPUT = 'Por Favor digite o valor: '

extrato = ""
LIMIT_DRAW_FOR_DAY = 500.0
AMOUT_DRAW_FOR_DAY = 3
AGENCIA = "0001"
account = 0
account_controller = 0
numero_conta = 1
users = {}



while True:
    v = input(menu).lower()

    if v == 'd':
        sh.clear()
        ui = sh.convert_value(input(MSG_INPUT))
        try:
            account, extrato  = bank.deposit(
                account, ui, extrato
            )
        except RuntimeError as e:
            print(e)
        else:
            print('Operação feita com sucesso')
    elif v == 's':
        sh.clear()
        ui = sh.convert_value(input(MSG_INPUT))
        try:
            account, extrato, account_controller = bank.draw(
                saldo=account,
                valor=ui,
                extrato=extrato,
                limit=LIMIT_DRAW_FOR_DAY,
                numero_saques=account_controller,
                limite_saques=AMOUT_DRAW_FOR_DAY
            )
        except RuntimeError as e:
            print(e)
        else:
            print('Operação feita com sucesso')

    elif v == 'e':
        bank.show_extrato(account, extrato=extrato)
    elif v == 'a':
        result = bank.create_user(users)
        if result:
            print('Usuario criado com sucesso')
    elif v == 'b':
        result = bank.create_conta(users, numero_conta, AGENCIA)
        if result:
            print('Conta criada com sucesso')
            numero_conta += 1
    elif v == 'x':
        print('Saindo ...')
        break
    else:
        print('Erro Entrada invalida')

