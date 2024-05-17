# Classe UsuarioTelefone e o encapsulamento dos atributos nome, numero e plano:
class UsuarioTelefone:
    def __init__(self, nome, numero, plano):
        self._nome = nome
        self._numero = numero
        self._plano = plano

    @property
    def nome(self):
        return self._nome
    
    @property
    def numero(self):
        return self._nome
    
    @property
    def plano(self):
        return self._plano
    
    def verificar_saldo(self):
        return self.plano.saldo

    def fazer_chamada(self, destinatario, duracao):
        custo = self.plano.custo_chamada(duracao)

        if custo > self.plano.saldo:
            return 'Saldo insuficiente para fazer a chamada.'
        else:
            self.plano.deduzir_saldo(custo)
            return f'Chamada para {destinatario} realizada com sucesso. Saldo: ${self.plano.saldo:.2f}'

# Classe Pano, ela representa o plano de um usuário de telefone:
class Plano:

    def __init__(self, saldo_inicial):
        self.saldo = saldo_inicial
    
    def custo_chamada(self, duracao):
        custo = duracao*0.10
        return custo
    
    def deduzir_saldo(self, custo):
        self.saldo -= custo

# Classe UsuarioPrePago, aqui vemos a herança onde UsuarioPrePago herda os atributos e métodos da classe UsuarioTelefone:
class UsuarioPrePago(UsuarioTelefone):
    def __init__(self, nome, numero, saldo_inicial):
        super().__init__(nome, numero, Plano(saldo_inicial))


# Recebendo as informações do usuário:
nome = input()
numero = input()
saldo_inicial = float(input())

# Objeto de UsuarioPrePago com os dados fornecidos:
usuario_pre_pago = UsuarioPrePago(nome, numero, saldo_inicial)
destinatario = input()
duracao = int(input())

# Chama o método fazer_chamada do objeto usuario_pre_pago e imprime o resultado:
print(usuario_pre_pago.fazer_chamada(destinatario, duracao))
