def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Sair
    => """
    return input(f"Digite a opção desejada: \n {menu}")
 
def depositar(saldo,valor, extrato, /):  # essa barra significa que os argumentos antes desse caracter devem ser inseridos por posição
    if valor > 0:
        saldo = saldo + valor
        extrato += f"Depósito: +R$ {valor:.2f}\n"
        print("Depósito realizado.")
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato

def sacar(*, saldo, valor, extrato, qtd_saques, limite_saque): 
    if valor > 0:
        if qtd_saques > 2:
            print("O limite diário de três saques foi excedido.")
        elif valor > saldo:
            print(f"O valor que está tentando sacar é maior que o saldo atual de: R$ {saldo:.2f}")
        elif valor > 500: 
                print("O valor máximo permitido por saque é de R$ 500.00.")
        
        else:
            saldo = saldo - valor
            qtd_saques = qtd_saques + 1
            extrato += f"Saque: -R$ {valor:.2f}\n"
            print("Saque realizado!")    
    else:
        print("Operação falhou! O valor informado é inválido.")

    return saldo,extrato

def mostrar_extrato(saldo, /, *, extrato):
    print(extrato)
    print(f"Saldo Total: R$ {saldo:.2f}")

#Criar usuário

#Criar conta

def main():
    saldo = 800.00
    limite_saque = 3
    qtd_saques = 0
    #deposito = 0
    #saque = 0
    extrato = ""

    while True:
        opcao = menu()

        if opcao == "1":
            valor = float(input("Informe o valor do depósito: "))
            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "2": 
            valor = float(input("Digite o valor que deseja sacar: "))
            saldo, extrato = sacar(
                saldo = saldo,
                valor = valor,
                extrato = extrato,
                qtd_saques = qtd_saques,
                limite_saque = limite_saque
            )
    
        elif opcao == "3":
            mostrar_extrato(saldo, extrato = extrato)

        elif opcao == "4":
            print("Encerrando...")
            break

        else:
            print("Operação inválida. Digite novamente o número correspondente a operação que deseja realizar.")

main()