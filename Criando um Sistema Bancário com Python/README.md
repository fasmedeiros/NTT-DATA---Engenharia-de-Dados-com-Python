# Sistema de Gerenciamento de Conta Bancária

Este é um sistema simples de gerenciamento de conta bancária que permite ao usuário realizar operações de depósito, saque, extrato e sair do sistema. O programa inclui validação de entrada para garantir que os valores informados sejam válidos.

## Funcionalidades

- **Depositar**: Permite ao usuário adicionar dinheiro à sua conta.
- **Sacar**: Permite ao usuário retirar dinheiro da sua conta, com validação para saldo e limite.
- **Extrato**: Exibe todas as movimentações realizadas, incluindo depósitos e saques.
- **Sair**: Encerra o programa.

## Requisitos

- Python 3.x

## Uso

Ao executar o programa, você verá um menu com as seguintes opções:

```
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
```

### Passos para Uso

1. **Depositar**:

   1.1 Escolha 'd' e informe o valor que deseja depositar.

   1.2 O programa validará se o valor é positivo.

   1.3 Exemplo:
     ```plaintext
     Informe o valor do depósito: 500
     ```

2. **Sacar**:

   2.1 Escolha 's' e informe o valor que deseja sacar.

   2.2 O programa verificará:

   - Se você possui saldo suficiente.
   - Se o valor do saque não excede o limite definido.
   - Se você já atingiu o número máximo de saques permitidos.

   2.3 Exemplo:
     ```plaintext
     Informe o valor do saque: 300
     ```

3. **Extrato**:

   3.1 Escolha 'e' para visualizar o extrato de suas movimentações.

   3.2 O programa mostrará todos os depósitos e saques realizados, bem como o saldo atual.

   3.3 Exemplo:
     ```plaintext
     ==================== EXTRATO ====================
     Depósito: R$ 500.00
     Saque: R$ 200.00
     Saldo: R$ 300.00
     =================================================
     ```

4. **Sair**:

   4.1 Escolha 'q' para encerrar o programa.

   4.2 O programa sairá e você verá uma mensagem de despedida.

   4.3 Exemplo:
     ```plaintext
     Obrigado por usar o sistema. Até logo!
     ```

5. **Validação de Entrada**:

   5.1 O programa garante que todos os valores inseridos são números válidos e positivos.

   5.2 Se um valor inválido for inserido, uma mensagem de erro será exibida.

### Exemplo de Uso

```plaintext
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> d
Informe o valor do depósito: 500

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> s
Informe o valor do saque: 200

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> e
==================== EXTRATO ====================
Depósito: R$ 500.00
Saque: R$ 200.00
Saldo: R$ 300.00
=================================================

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> q
Obrigado por usar o sistema. Até logo!
```
