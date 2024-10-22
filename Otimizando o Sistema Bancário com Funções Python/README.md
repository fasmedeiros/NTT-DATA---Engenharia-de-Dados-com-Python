# Sistema Bancário Simples em Python

Este projeto implementa um sistema bancário simples em Python que permite realizar operações como depósito, saque, extrato, criação de usuários e contas. A seguir, são apresentadas as principais funcionalidades e o funcionamento do código.

## Funcionalidades

- **Depositar**: Permite ao usuário realizar depósitos na conta.
- **Sacar**: Permite ao usuário sacar valores, respeitando limites de saldo e número de saques.
- **Extrato**: Exibe o extrato das movimentações realizadas na conta.
- **Criar Usuário**: Permite o cadastro de novos usuários no sistema.
- **Criar Conta**: Permite a criação de uma nova conta associada a um usuário.
- **Listar Contas**: Exibe a lista de contas criadas.

## Estrutura do Código

### Funções

- `menu()`: Exibe o menu de opções para o usuário.
- `depositar(saldo, valor, extrato)`: Realiza o depósito de um valor na conta.
- `sacar(saldo, valor, extrato, limite, numero_saques, limite_saques)`: Realiza o saque de um valor, verificando limites de saldo e número de saques.
- `exibir_extrato(saldo, extrato)`: Exibe o extrato da conta e o saldo atual.
- `validar_cpf(cpf)`: Valida o CPF do usuário, garantindo que tenha 11 dígitos.
- `criar_usuario(usuarios)`: Cria um novo usuário, garantindo que o CPF não esteja cadastrado e seja válido.
- `filtrar_usuario(cpf, usuarios)`: Filtra e retorna um usuário pelo CPF.
- `criar_conta(agencia, numero_conta, usuarios)`: Cria uma nova conta associada a um usuário existente.
- `listar_contas(contas)`: Lista todas as contas criadas.

### Exemplo de Uso

1. O usuário é apresentado a um menu de opções.
2. O usuário pode escolher realizar depósitos, saques, visualizar o extrato, criar novos usuários ou contas, e listar contas existentes.
3. As operações são realizadas, e o sistema retorna mensagens de sucesso ou erro conforme a situação.

### Validações Implementadas

- Verificação se o CPF possui 11 dígitos.
- Tratamento de exceções ao solicitar valores de depósitos e saques, garantindo que entradas inválidas sejam tratadas.

## Execução

Para executar o sistema, basta rodar o script Python. O usuário interage através do terminal, digitando as opções desejadas.

## Contribuição

Sinta-se à vontade para contribuir com melhorias ou novos recursos. Críticas e sugestões são bem-vindas!
