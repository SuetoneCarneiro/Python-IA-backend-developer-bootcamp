from abc import ABC, abstractmethod
from datetime import datetime

class Cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class PessoaFisica(Cliente):
    def __init__(self, cpf, nome, data_nascimento, endereco):
        super().__init__(endereco)
        self.cpf = cpf
        self.nome = nome
        self.data_nascimento = data_nascimento


class Conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = '0001'
        self._cliente = cliente
        self._historico = Historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    @property
    def saldo(self):
        return self._saldo
    
    @property
    def numero(self):
        return self._numero
    
    @property
    def agencia(self):
        return self._agencia
    
    @property
    def cliente(self):
        return self._cliente
    
    @property
    def historico(self):
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo

        if valor > saldo or saldo == 0:
            print('\033[31mFALHA NA OPERAÇÃO: Saldo insuficiente.\033[m')
        elif valor > 0:
            self._saldo -= valor
            print('\033[32mContando cédulas...\nRetire seu dinheiro na boca do caixa.\033[m')
            return True
        else:
            print(f'\033[31mERRO: Valor inválido.\033[m')
        
        return False


    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print('\033[32mDepósito realizado com sucesso!\033[m')
        else:
            print('\033[31mERRO! Valor inválido. Tente novamente.\033[m')
            return False
        return True
            

class ContaCorrente(Conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    def sacar(self, valor): # necessário para lidar com os limites de quantidade e valor de saque
        numero_saques = len(
            [transacao for transacao in self.historico.transacoes if transacao["tipo"] == Saque.__name__]
        )

        if valor > self.limite:
            print(f'\033[31mO limite por saque é de R${self.limite:.2f}\nTente novamente.\033[m')

        elif numero_saques >= self.limite_saques:
            print('''\033[31mVocê atingiu o limite de saques diário.\n
                  Por favor, aguarde até o próximo dia para realizar o saque\033[m''')

        else:
            return super().sacar(valor)

        return False

    def __str__(self):
        return f'Agência: {self.agencia}\nConta: {self.numero}\nTitular: {self.cliente.nome}'


class Historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def adicionar_transacao(self, transacao):
        self._transacoes.append(
            {
                'tipo' : transacao.__class__.__name__,
                'valor': transacao.valor,
                'data': datetime.now().strftime('%d-%m-%Y %H:%M:%s'),
            }
        )
    

class Transacao(ABC): # essa é uma classe abstrata - interface
    @property
    @abstractmethod
    def valor(self):
        pass

    @classmethod
    def registrar(cls, conta):
        pass


class Saque(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @classmethod
    def registrar(cls, conta):
        if conta.sacar(cls.valor):
            conta.historico.adicionar_transacao(cls)


class Deposito(Transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    @classmethod
    def registrar(cls, conta):
        if conta.depositar(cls.valor):
            conta.historico.adicionar_transacao(cls)
