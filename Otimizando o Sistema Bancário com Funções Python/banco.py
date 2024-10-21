<<<<<<< HEAD
import re

# Dados principais
usuarios = []
contas = []
AGENCIA_PADRAO = "0001"
numero_conta_sequencial = 1

# Funções de Operações Bancárias

def depositar(saldo, valor, extrato):
    """
    Realiza um depósito na conta.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser depositado.
        extrato (str): Histórico de transações.

    Returns:
        tuple: Novo saldo e histórico de extrato atualizado.
    """
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta.

    Keyword Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser sacado.
        extrato (str): Histórico de transações.
        limite (float): Limite por saque.
        numero_saques (int): Número atual de saques realizados.
        limite_saques (int): Limite máximo de saques permitidos.

    Returns:
        tuple: Novo saldo e histórico de extrato atualizado.
    """
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    """
    Exibe o extrato da conta.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico de transações.
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funções de Gerenciamento de Usuários e Contas

def criar_usuario():
    """
    Cadastra um novo usuário no sistema.
    """
    print("\n=== Cadastro de Usuário ===")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o CPF (apenas números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Validar CPF (apenas números)
    if not cpf.isdigit():
        print("CPF inválido! Deve conter apenas números.")
        return

    # Verificar se CPF já existe
    if filtrar_usuario(cpf, usuarios):
        print("Já existe usuário com esse CPF!")
        return

    # Adicionar usuário
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    """
    Busca um usuário pelo CPF.

    Args:
        cpf (str): CPF do usuário a ser buscado.
        usuarios (list): Lista de usuários.

    Returns:
        dict or None: Usuário encontrado ou None se não encontrado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, contas, usuarios):
    """
    Cria uma nova conta bancária vinculada a um usuário existente.

    Args:
        agencia (str): Agência da conta.
        contas (list): Lista de contas existentes.
        usuarios (list): Lista de usuários existentes.
    """
    global numero_conta_sequencial
    print("\n=== Criação de Conta ===")
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado! Favor cadastrar o usuário antes de criar a conta.")
        return

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta_sequencial,
        "usuario": usuario
    }
    contas.append(conta)
    numero_conta_sequencial += 1
    print(f"Conta criada com sucesso! Número da conta: {conta['numero_conta']}")

def listar_contas(contas):
    """
    Lista todas as contas cadastradas.

    Args:
        contas (list): Lista de contas existentes.
    """
    print("\n=== Listagem de Contas ===")
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | "
              f"Titular: {conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}")

# Função Principal

def main():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia = AGENCIA_PADRAO

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            valor = ler_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = ler_valor("Informe o valor do saque: ")
            resultado = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            if resultado:
                saldo, extrato, numero_saques = resultado

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta(agencia, contas, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def ler_valor(mensagem):
    """
    Lê um valor do usuário, garantindo que seja um número positivo.

    Args:
        mensagem (str): Mensagem a ser exibida para o usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Operação falhou! O valor informado deve ser maior que zero.")
        except ValueError:
            print("Operação falhou! Por favor, informe um número válido.")

if __name__ == "__main__":
    main()
=======
import re

# Dados principais
usuarios = []
contas = []
AGENCIA_PADRAO = "0001"
numero_conta_sequencial = 1

# Funções de Operações Bancárias

def depositar(saldo, valor, extrato):
    """
    Realiza um depósito na conta.

    Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser depositado.
        extrato (str): Histórico de transações.

    Returns:
        tuple: Novo saldo e histórico de extrato atualizado.
    """
    saldo += valor
    extrato += f"Depósito: R$ {valor:.2f}\n"
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    """
    Realiza um saque da conta.

    Keyword Args:
        saldo (float): Saldo atual da conta.
        valor (float): Valor a ser sacado.
        extrato (str): Histórico de transações.
        limite (float): Limite por saque.
        numero_saques (int): Número atual de saques realizados.
        limite_saques (int): Limite máximo de saques permitidos.

    Returns:
        tuple: Novo saldo e histórico de extrato atualizado.
    """
    if valor > saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        return saldo, extrato, numero_saques
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    """
    Exibe o extrato da conta.

    Args:
        saldo (float): Saldo atual da conta.
        extrato (str): Histórico de transações.
    """
    print("\n================ EXTRATO ================")
    if not extrato:
        print("Não foram realizadas movimentações.")
    else:
        print(extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

# Funções de Gerenciamento de Usuários e Contas

def criar_usuario():
    """
    Cadastra um novo usuário no sistema.
    """
    print("\n=== Cadastro de Usuário ===")
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    cpf = input("Informe o CPF (apenas números): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    # Validar CPF (apenas números)
    if not cpf.isdigit():
        print("CPF inválido! Deve conter apenas números.")
        return

    # Verificar se CPF já existe
    if filtrar_usuario(cpf, usuarios):
        print("Já existe usuário com esse CPF!")
        return

    # Adicionar usuário
    usuarios.append({
        "nome": nome,
        "data_nascimento": data_nascimento,
        "cpf": cpf,
        "endereco": endereco
    })
    print("Usuário criado com sucesso!")

def filtrar_usuario(cpf, usuarios):
    """
    Busca um usuário pelo CPF.

    Args:
        cpf (str): CPF do usuário a ser buscado.
        usuarios (list): Lista de usuários.

    Returns:
        dict or None: Usuário encontrado ou None se não encontrado.
    """
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def criar_conta(agencia, contas, usuarios):
    """
    Cria uma nova conta bancária vinculada a um usuário existente.

    Args:
        agencia (str): Agência da conta.
        contas (list): Lista de contas existentes.
        usuarios (list): Lista de usuários existentes.
    """
    global numero_conta_sequencial
    print("\n=== Criação de Conta ===")
    cpf = input("Informe o CPF do usuário: ")

    usuario = filtrar_usuario(cpf, usuarios)

    if not usuario:
        print("Usuário não encontrado! Favor cadastrar o usuário antes de criar a conta.")
        return

    conta = {
        "agencia": agencia,
        "numero_conta": numero_conta_sequencial,
        "usuario": usuario
    }
    contas.append(conta)
    numero_conta_sequencial += 1
    print(f"Conta criada com sucesso! Número da conta: {conta['numero_conta']}")

def listar_contas(contas):
    """
    Lista todas as contas cadastradas.

    Args:
        contas (list): Lista de contas existentes.
    """
    print("\n=== Listagem de Contas ===")
    if not contas:
        print("Não há contas cadastradas.")
        return

    for conta in contas:
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | "
              f"Titular: {conta['usuario']['nome']} | CPF: {conta['usuario']['cpf']}")

# Função Principal

def main():
    menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[nu] Novo Usuário
[nc] Nova Conta
[lc] Listar Contas
[q] Sair

=> """

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    agencia = AGENCIA_PADRAO

    while True:
        opcao = input(menu).strip().lower()

        if opcao == "d":
            valor = ler_valor("Informe o valor do depósito: ")
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = ler_valor("Informe o valor do saque: ")
            resultado = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES
            )
            if resultado:
                saldo, extrato, numero_saques = resultado

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario()

        elif opcao == "nc":
            criar_conta(agencia, contas, usuarios)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("Obrigado por usar o sistema. Até logo!")
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

def ler_valor(mensagem):
    """
    Lê um valor do usuário, garantindo que seja um número positivo.

    Args:
        mensagem (str): Mensagem a ser exibida para o usuário.

    Returns:
        float: Valor informado pelo usuário.
    """
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0:
                return valor
            else:
                print("Operação falhou! O valor informado deve ser maior que zero.")
        except ValueError:
            print("Operação falhou! Por favor, informe um número válido.")

if __name__ == "__main__":
    main()
>>>>>>> c7dce54f73d91087a27f7cbf40a57172a11e50f2
