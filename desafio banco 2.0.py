import textwrap

# Constantes globais
AGENCIA = "0001"
LIMITE_SAQUES = 3
LIMITE_VALOR_SAQUE = 500 # Limite por saque individual, não total


def menu():
    menu_texto = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu_texto))


def depositar(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito:\tR$ {valor:.2f}\n"
        print("\n=== Depósito realizado com sucesso! ===")
    else:
        print("\n@@@ Operação falhou! O valor informado é inválido. @@@")
    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    # Validação do saque por cédulas (múltiplo de R$ 5,00)
    if valor <= 0 or valor % 5 != 0:
        print("\n@@@ Operação falhou! O valor do saque deve ser positivo e múltiplo de R$ 5,00 (ex: 5, 10, 15, ...). @@@")
        return saldo, extrato, numero_saques # Retorna os valores inalterados

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= limite_saques

    if excedeu_saldo:
        print("\n@@@ Operação falhou! Você não tem saldo suficiente. @@@")
    elif excedeu_limite:
        print(f"\n@@@ Operação falhou! O valor do saque excede o limite de R$ {limite:.2f}. @@@")
    elif excedeu_saques:
        print("\n@@@ Operação falhou! Número máximo de saques excedido. @@@")
    else:
        saldo -= valor
        extrato += f"Saque:\t\tR$ {valor:.2f}\n"
        numero_saques += 1
        print("\n=== Saque realizado com sucesso! ===")
    return saldo, extrato, numero_saques


def exibir_extrato(saldo, /, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo:\t\tR$ {saldo:.2f}")
    print("==========================================")


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente números): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("\n=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário para associar a conta: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n=== Conta criada com sucesso! ===")
        # Ao criar a conta, inicializamos os dados financeiros dela
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "extrato": "", "numero_saques": 0}
    else:
        print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")
        return None


def listar_contas(contas):
    if not contas:
        print("\n@@@ Nenhuma conta cadastrada ainda. @@@")
        return

    print("\n================ LISTA DE CONTAS ================")
    for i, conta in enumerate(contas):
        print(f"Conta {i+1}:")
        linha = f"""\
            Agência:\t\t{conta['agencia']}
            C/C:\t\t{conta['numero_conta']}
            Titular:\t\t{conta['usuario']['nome']}
            CPF do Titular:\t{conta['usuario']['cpf']}
        """
        print(textwrap.dedent(linha))
        print("-" * 50)
    print("=================================================")


def main():
    # LIMITE_SAQUES = 3
    # AGENCIA = "0001"
    
    # Estas são as variáveis da "conta principal" ou "conta ativa" da sessão
    # que o código original manipulava para depósito, saque e extrato.
    # Elas PRECISAM ser inicializadas ANTES do loop.
    saldo = 0
    extrato = ""
    numero_saques = 0
    
    # As listas de usuários e contas
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))
            # Aqui, `LIMITE_VALOR_SAQUE` é o limite por saque, e `LIMITE_SAQUES` é o total de saques.
            saldo, extrato, numero_saques = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=LIMITE_VALOR_SAQUE, # Passa a constante como limite por saque
                numero_saques=numero_saques,
                limite_saques=LIMITE_SAQUES, # Passa a constante para o limite de saques
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            # Passa a constante AGENCIA aqui
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            print("\nSaindo do sistema. Obrigado por usar nosso banco!")
            break

        else:
            print("\n@@@ Operação inválida, por favor selecione novamente a operação desejada. @@@")


if __name__ == "__main__":
    main()