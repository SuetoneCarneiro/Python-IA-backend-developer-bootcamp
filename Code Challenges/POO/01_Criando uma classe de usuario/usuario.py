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
    

    # A classe `UsuarioTelefone` define um método especial `__str__`, que retorna uma representação em string do objeto.
    def __str__(self):
        return f"Usuário {self.nome} criado com sucesso."


# Entrada:
nome = input()  
numero = input()  
plano = input()  

usuario = UsuarioTelefone(nome, numero, plano)

print(usuario)
