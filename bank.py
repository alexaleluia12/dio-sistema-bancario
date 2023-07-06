import share as sh

def draw(*,saldo, valor, extrato, limit, numero_saques, limite_saques):

    if valor <= 0:
        raise RuntimeError('Erro - Valor precisa ser maior que 0.')
    if numero_saques >= limite_saques:
        raise RuntimeError('Erro - Atingiu número maximo de saques por dia.')
    if valor > limit:
        raise RuntimeError(f"Erro - Máximo por saque é R$ {limite_saques:.2f}")
    if (saldo - valor) <= 0.0:
        raise RuntimeError("Erro - Saldo negativo para esse valor.")
    saldo -= valor
    numero_saques += 1
    extrato += f"Saque = R$ {valor:.2f}\n"

    return saldo, extrato, numero_saques

def deposit(saldo, valor, extrato):
    if valor <= 0:
        raise RuntimeError('Erro - Valor precisa ser maior que 0.')

    saldo += valor
    extrato += f"Deposito = R$ {valor:.2f} \n"

    return saldo, extrato

def show_extrato(saldo, *, extrato):
    print(f'Saldo = R$ {saldo:.2f}')
    print(extrato)

def create_user(users: dict):
    sh.clear()
    print("Cadastro de Usuário")
    cpf = input("Informe o CPF: ")
    if cpf in users:
        print("Erro - Usuário com esse CPF já existe")
        return False
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento: ")
    endereco = input("Informe o endereco: ")
    users[cpf] = {'nome': nome, 'data_nascimento': data_nascimento, 'endereco': endereco, 'contas': []}
    return True

def create_conta(users, cc, agencia):
    sh.clear()
    print("Cadastro de Conta")
    cpf = input("Informe o CPF: ")
    if cpf not in users:
        print("Erro - Cliente não existe, é necessário fazer o Cadastro")
        return False
    user = users[cpf]
    user['contas'].append({'agencia': agencia, 'numero_conta': cc})
    return True
