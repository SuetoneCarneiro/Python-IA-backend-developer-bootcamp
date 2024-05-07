from os import system
from time import sleep
from textwrap import dedent

def limpar_terminal():
    sleep(3)
    system("clear")

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f'Depósito: R$ {valor:.2f}\n'
        print('\033[32mDepósito realizado com sucesso!\033[m')
    else:
        print('\033[31mERRO! Valor inválido. Tente novamente.\033[m')
        limpar_terminal()
    
    return saldo, extrato
    
def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques == limite_saques: # atingiu o limite de saques diário
        print('\033[31mVocê atingiu o limite de saques diário.\nPor favor, aguarde até o próximo dia para realizar o saque\033[m')
        limpar_terminal()

        return saldo, extrato

    if valor >= limite: # solicitou um valor acima do limite por saque
        print(f'\033[31mO limite por saque é de R${limite:.2f}\nTente novamente.\033[m')
        limpar_terminal()

        return saldo, extrato
    
    if valor > saldo or saldo == 0: # não possui saldo para sacar
        print('\033[31mNão será possível realizar o saque pois não há saldo suficiente.\033[m')
        limpar_terminal()

        return saldo, extrato
    
    if saldo > valor: # operação válida
        print('\033[32mContando cédulas...\nRetire seu dinheiro na boca do caixa.\033[m')
        saldo -= valor
        numero_saques += 1
        extrato += f'Saque: R$ {valor:.2f}\n'

        return saldo, extrato

def ver_extrato(saldo, /, *, extrato):
    print('-'*50)
    print('Não houveram movimentações' if not extrato else extrato)
    print(f'Saldo: R$ {saldo:.2f}')
    print('-'*50)

def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_usuario(usuarios):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('\033[31mUsuário já cadastrado!\033[m')
        limpar_terminal()
        return
    
    nome = input('Nome completo: ')
    data_nascimento = input('Data  de nascimento (dd-mm-aaaa): ')
    endereco = input('Endereço (logradouro, número - bairro - cidade/sigla do estado)): ')

    usuarios.append({'nome':nome, 'cpf':cpf, 'data_nascimento':data_nascimento, 'endereco':endereco})
    print('\033[32mUsuário cadastrado com sucesso!\033[m')

def criar_conta(*, usuarios, numero_da_conta, agencia):
    cpf = input('Informe o CPF (apenas números): ')
    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print('\033[31mUsuário não cadastrado!Realize o cadastro primeiro.\033[m')
        limpar_terminal()
        return
    
    print('\033[32mConta criada com sucesso!\033[m')
    return {'agencia':agencia, 'numero_da_conta':numero_da_conta, 'usuario':usuario}

def listar_contas(contas):
    for conta in contas:
        info = f'''\
            Agência: {conta['agencia']}
            C/C: {conta['numero_da_conta']}
            Titular: {conta['usuario']['nome']}
        '''
        print("-" * 30)
        print(dedent(info))
        print("-" * 30)

def listar_usuarios(usuarios):
    for usuario in usuarios:
        info = f'''\
            Nome: {usuario['nome']}
            CPF: {usuario['cpf']}
            Data de nascimento: {usuario['data_nascimento']}
            Endereço: {usuario['endereco']}
        '''
        print("-" * 40)
        print(dedent(info))
        print("-" * 40)
        sleep(3)
    
def menu():
    menu=''' 
    ------ DIO Bank ------

    [1] Realizar depósito
    [2] Realizar saque
    [3] Ver extrato
    [4] Criar usuário
    [5] Criar conta
    [6] Listar contas
    [7] Listar usuarios
    [8] Sair

    >> '''
    menu = dedent(menu)
    return menu
        
def main():
    LIMITE_SAQUES = 3
    AGENCIA = '0001'

    saldo = 0
    limite_por_saque = 500
    saques_realizados = 0
    extrato = ''

    usuarios = []
    contas = []
    
    while True:
        opcao = input(menu())

        match opcao:
            case '1':
                valor = float(input('Valor do depósito: R$ '))
                saldo, extrato = deposito(saldo, valor, extrato)
            case '2':
                valor = float(input('Valor do saque: R$ '))
                saldo, extrato = saque(saldo=saldo,
                      valor=valor,
                      extrato=extrato,
                      limite=limite_por_saque,
                      numero_saques=saques_realizados,
                      limite_saques=LIMITE_SAQUES
                    )
                saques_realizados += 1
            case '3':
                ver_extrato(saldo, extrato=extrato)
            case '4':
                criar_usuario(usuarios)
            case '5':
                numero_da_conta  = len(contas) + 1
                conta = criar_conta(usuarios=usuarios, numero_da_conta=numero_da_conta, agencia=AGENCIA)
                if conta:
                    contas.append(conta)
            case '6':
                listar_contas(contas)
            case '7':
                listar_usuarios(usuarios)
            case '8':
                break
            case _:
                print('\033[31mOpção inválida. Tente novamente.\033[m')

    print(f'\033[33mO DIO Bank agradece a sua preferência!\033[m')

main()
