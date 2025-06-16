def depositar(saldo, extrato):
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES):
    valor = float(input("Informe o valor do saque: "))

    if valor <= 0 or valor % 5 != 0:
        print("Operação falhou! O valor do saque deve ser positivo e múltiplo de R$ 5,00 (ex: 5, 10, 15, ...).")
        return saldo, extrato, numero_saques

    excedeu_saldo = valor > saldo
    excedeu_limite = valor > limite
    excedeu_saques = numero_saques >= LIMITE_SAQUES

    if excedeu_saldo:
        print("Operação falhou! Você não tem saldo suficiente.")
    elif excedeu_limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif excedeu_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    else:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print("Saque realizado com sucesso!")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

def main():
    menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

    saldo = 0
    limite = 5000
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 5 # Constante para o limite de saques

    while True:
        opcao = input(menu)

        if opcao == "d":
            saldo, extrato = depositar(saldo, extrato)
        elif opcao == "s":
            saldo, extrato, numero_saques = sacar(saldo, limite, extrato, numero_saques, LIMITE_SAQUES)
        elif opcao == "e":
            exibir_extrato(saldo, extrato)
        elif opcao == "q":
            print("Saindo do sistema. Obrigado por usar nosso banco!")
            break
        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")

# Chama a função principal para iniciar o programa
main()