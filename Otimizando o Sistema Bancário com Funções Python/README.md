# Sistema Bancário Modularizado

## Objetivo
Este projeto tem como objetivo desenvolver um sistema bancário modularizado com funções separadas para realizar operações bancárias e gerenciar usuários e contas. Além disso, o código será estruturado para seguir boas práticas de programação, utilizando passagem de argumentos de diferentes formas, como `keyword only` e `positional only`.

## Funcionalidades
O sistema bancário possui as seguintes operações:

1. **Cadastrar Usuário (Cliente do Banco)**
   - Um usuário é composto por:
     - Nome
     - Data de Nascimento
     - CPF (somente os números)
     - Endereço (formato: "logradouro, número - bairro - cidade / estado")
   - Um CPF não pode ser duplicado no sistema.

2. **Cadastrar Conta Corrente**
   - Cada conta é composta por:
     - Agência (número fixo: "0001")
     - Número da Conta (sequencial, iniciando em 1)
     - Usuário (vinculado pelo CPF)
   - Um usuário pode ter mais de uma conta, mas uma conta pertence a um único usuário.

3. **Sacar Dinheiro**
   - Operação realizada utilizando apenas argumentos nomeados (`keyword only`).
   - Sugestão de argumentos:
     - `saldo`: Saldo disponível.
     - `valor`: Valor a ser sacado.
     - `extrato`: Histórico de transações.
     - `limite`: Limite de saque.
     - `numero_saques`: Contador de saques realizados.
     - `limite_saques`: Número máximo de saques permitidos.
   - Retorno: Saldo atualizado e extrato.

4. **Depositar Dinheiro**
   - Operação realizada utilizando apenas argumentos posicionais (`positional only`).
   - Sugestão de argumentos:
     - `saldo`: Saldo disponível.
     - `valor`: Valor a ser depositado.
     - `extrato`: Histórico de transações.
   - Retorno: Saldo atualizado e extrato.

5. **Visualizar Extrato**
   - Operação realizada com argumentos tanto posicionais quanto nomeados.
   - Argumentos posicionais: `saldo`.
   - Argumentos nomeados: `extrato`.
   
6. **Listar Contas**
   - Exibe as contas cadastradas e seus respectivos usuários.

## Regras de Negócio
- Não é possível cadastrar dois usuários com o mesmo CPF.
- O número da conta é sequencial, começando em 1.
- Um usuário pode ter várias contas, mas cada conta pertence a um único usuário.
- A função de saque só pode ser chamada com argumentos nomeados, a de depósito com argumentos posicionais, e a de visualização do extrato utiliza uma combinação de ambos.

## Estrutura do Sistema

- `cadastrar_usuario(nome, nascimento, cpf, endereco)`  
  Função para cadastrar um novo usuário. Valida a unicidade do CPF e armazena o usuário em uma lista.

- `cadastrar_conta(cpf)`  
  Função para cadastrar uma nova conta para um usuário existente. O CPF é utilizado para buscar o usuário.

- `sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`  
  Função para realizar saques, controlando o saldo, o limite e o número de saques permitidos.

- `depositar(saldo, valor, extrato, /)`  
  Função para realizar depósitos, atualizando o saldo e o extrato.

- `visualizar_extrato(saldo, *, extrato)`  
  Função para exibir o saldo e o extrato da conta.

- `listar_contas()`  
  Função que exibe todas as contas cadastradas e os usuários vinculados.

## Exemplo de Uso

```python
# Cadastrando um novo usuário
cadastrar_usuario("João Silva", "01/01/1990", "12345678900", "Rua A, 123 - Centro - Cidade / SP")

# Cadastrando uma conta para o usuário João
cadastrar_conta("12345678900")

# Realizando um depósito
saldo, extrato = depositar(1000, 200, [])

# Realizando um saque
saldo, extrato = sacar(saldo=saldo, valor=300, extrato=extrato, limite=500, numero_saques=0, limite_saques=3)

# Visualizando o extrato
visualizar_extrato(saldo, extrato=extrato)

# Listando todas as contas
listar_contas()
