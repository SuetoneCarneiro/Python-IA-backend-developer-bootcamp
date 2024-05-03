from os import system
from time import sleep

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
    
    if opcao == '1':
        valor = float(input('Valor do depósito: R$ '))

        if valor > 0:
            saldo += valor
            extrato += f'Depósito #{cont_depositos}: R$ {valor:.2f}'
            cont_depositos += 1
            print('\033[32mDepósito realizado com sucesso!\033[m')
        else:
            print('\033[31mERRO! Valor inválido. Tente novamente.\033[m')
            sleep(3)
            system("clear")

    if opcao == '2':
        pass

    if opcao == '3':
        pass

    if opcao == '4':
        pass
    