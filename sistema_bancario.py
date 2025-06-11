menu = """
[1] Depositar
[2] Sacar
[3] Extrato
[4] Sair
"""

saldo = 800.00
limite_saque = 3
qtd_saques = 0
deposito = 0
saque = 0
extrato = ""

while True:
    print("Digite a opção desejada: \n", menu)
    opcao = input("=> ")

    if opcao == "1":
        deposito = float(input("Informe o valor do depósito: "))
        saldo = saldo + deposito
        extrato += f"Depósito: +R$ {deposito:.2f}\n"
        print("Depósito realizado.")

    elif opcao == "2": 
        saque = float(input("Digite o valor que deseja sacar: "))
        if qtd_saques > 2:
            print("O limite diário de três saques foi excedido.")
        
        elif saque > saldo:
            print(f"O valor que está tentando sacar é maior que o saldo atual de: R$ {saldo:.2f}")
        
        elif saque > 500: 
            print("O valor máximo permitido por saque é de R$ 500.00.")
        
        else:
            saldo = saldo - saque
            qtd_saques = qtd_saques + 1
            extrato += f"Saque: -R$ {saque:.2f}\n"
            print("Saque realizado!")
    
    elif opcao == "3":
        print(extrato)
        print(f"Saldo Total: R$ {saldo:.2f}")

    elif opcao == "4":
        print("Encerrando...")
        break

    else:
        print("Operação inválida. Digite novamente o número correspondente a operação que deseja realizar.")