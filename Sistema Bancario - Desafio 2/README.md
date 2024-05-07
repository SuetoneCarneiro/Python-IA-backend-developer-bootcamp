# Objetivo geral do desafio
- Criar um sistema bancário com as operações: sacar, depositar e visualizar extrato
- Separar as funcionalidades existentes de saque, depósito e extrato em funções. 
- Criar duas novas funções: cadastrar usuário(cliente) e cadastrar conta bancária.


## Resquisitos

### Saque
- A função saque deve receber argumentos apenas por nome (keyword only). 
- Sugetão de argumentos: saldo, valor, extrato, limite, numero_saques, limite_saques.
- Sugestão de retorno: saldo e extrato.

### Depósito
- A função depósito deve receber os argumentos apenas por posição (positional only). 
- Sugestão de argumentos: saldo, valor, extrato.
- Sugestão de retorno: saldo e extrato.

### Extrato
- A função extrato deve receber os argumentos por posição e nome (positional ony and keyword only).
- Argumentos posicionais: saldo
- Argumentos nomeados: extrato.

## Novas funções

### Criar usuário
- O programa deve armazenar os usuários em uma lista. Um usuário é composto por: nome, data de nascimento, cpf e endereço. Endereço é uma string com o formato: logradouro, número - bairro - cidade/sigla do estado. Deve ser armazenado somente números do CPF. Não podemos cadastrar 2 usuários com o mesmo CPF.

### Criar conta
- O programa deve armazenar constas em uma lista. Uma conta é composta por: agência, número da conta e usuário. O número da conta é sequencial, iniciando em 1. O número da agência é fixo: '0001'. O usuário pode ter mais de uma conta, mas uma conta pertence a apenas um usuário.

Dica extra: Para vincular uma conta, filtre a lista de usuários buscando o número do CPF informado para cada usuário da lista.