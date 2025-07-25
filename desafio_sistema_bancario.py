menu = """
[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair
=> """

saldo = 0
limite = 500
extrato = ""
numero_saques = 0
LIMITE_SAQUES = 3

def depositar(saldo, extrato):
    valor_input = input("Informe o valor do depósito: ")
    
    # Verifica se o input é numérico
    if valor_input.replace('.', '', 1).isdigit():
        valor = round(float(valor_input), 2)
        
        if valor > 0:
            saldo += valor
            extrato += f"- Depósito: R$ {valor:.2f}\n"
        elif valor == 0:
            print("Erro: Valor não pode ser zero.")
        else:
            print("Erro: Valor deve ser positivo.")
    else:
        print("Erro: Insira um número válido.")
    
    return saldo, extrato

def sacar(saldo, extrato, numero_saques, limite=500, LIMITE_SAQUES=3):
    valor_input = input("Informe o valor do saque: ")
    
    # Verifica se o valor é numérico 
    if valor_input.replace('.', '', 1).isdigit():
        valor = round(float(valor_input), 2)
        
        excedeu_saldo = valor > saldo
        excedeu_limite = valor > limite
        excedeu_saques = numero_saques >= LIMITE_SAQUES
        
        if excedeu_saldo:
            print("Erro: Saldo insuficiente.")
        elif excedeu_limite:
            print(f"Erro: Limite por saque é R$ {limite:.2f}.")
        elif excedeu_saques:
            print("Erro: Limite diário de saques atingido.")
        elif valor > 0:
            saldo -= valor
            extrato += f"- Saque: R$ {valor:.2f}\n"
            numero_saques += 1
        else:
            print("Erro: Valor deve ser positivo.")
    else:
        print("Erro: Insira um número válido.")
    
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, extrato):
    print("\n" + "=" * 40)
    print("EXTRATO".center(40))
    print("=" * 40)
    print(extrato if extrato else "Nenhuma movimentação.")
    print(f"\nSaldo atual: R$ {saldo:.2f}".center(40))
    print("=" * 40)

while True:
    opcao = input(menu).strip().lower()

    if opcao == "d":
        saldo, extrato = depositar(saldo, extrato)
    elif opcao == "s":
        saldo, extrato, numero_saques = sacar(saldo, extrato, numero_saques)
    elif opcao == "e":
        exibir_extrato(saldo, extrato)
    elif opcao == "q":
        break
    else:
        print("Opção inválida. Tente novamente.")