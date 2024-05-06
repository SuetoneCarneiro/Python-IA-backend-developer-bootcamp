from os import system
from time import sleep

def limpar_terminal():
    sleep(3)
    system("clear")

menu=''' 
------ DIO Bank ------

[1] Realizar depósito
[2] Realizar saque
[3] Ver extrato
[4] Sair

>> '''

saldo = 0
LIMITE_SAQUES = 3
limite_por_saque = 500
saques_realizados = 0
extrato = ''
cont_depositos = 1

while True:
    opcao = input(menu)

    if opcao not in '1234':
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        continue
    
    if opcao == '1': # Depósitos
        valor = float(input('Valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito #{cont_depositos}: R$ {valor:.2f}' + '\n'
            cont_depositos += 1
            print('\033[32mDepósito realizado com sucesso!\033[m')
        else:
            print('\033[31mERRO! Valor inválido. Tente novamente.\033[m')
            limpar_terminal()

    if opcao == '2': # Saques
        if saques_realizados == LIMITE_SAQUES:
            print('\033[31mVocê atingiu o limite de saques diário.\nPor favor, aguarde até o próximo dia para realizar o saque\033[m')
            limpar_terminal()
            continue
        
        valor = float(input('Valor do saque: R$ '))

        if valor > limite_por_saque:
            print(f'\033[31mO limite por saque é de R${limite_por_saque}\nTente novamente.\033[m')
            limpar_terminal()
            continue

        if valor > saldo or saldo == 0:
            print('\033[31mNão será possível realizar o saque pois não há saldo suficiente.\033[m')
            limpar_terminal()
            continue

        if saldo > valor:
            print('\033[32mContando cédulas...\nRetire seu dinheiro na boca do caixa.\033[m')
            saldo -= valor
            saques_realizados += 1
            extrato += f'Saque #{saques_realizados}: R$ {valor:.2f}' + '\n'

    if opcao == '3': # Extrato
        if not extrato:
            print('Não foram realizadas movimentações')
        else:
            print('-'*25)
            print(extrato)
            print(f'Saldo atual: R$ {saldo:.2f}')
            print('-'*25)
            sleep(3)

    if opcao == '4': # Sair
        break

print(f'\033[33mO DIO Bank agradece a sua preferência!\033[m')
