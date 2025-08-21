def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Sair
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

def criar_usuario(usuarios):
    cpf = input("Informe seu CPF sem pontos: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("Usuário já cadastrado!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento no formato dd-mm-aaaa: ")
    endereco = input("Informe o endereço no formato logradouro, número - bairro - cidade/uf: ")

    usuarios.append({"nome": nome,"data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    print("Usuário cadastrado com sucesso!")

def validar_usuario(cpf, usuarios):
    usuario_filtrado = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
    return usuario_filtrado[0] if usuario_filtrado else None

def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe seu CPF sem pontos: ")
    usuario = validar_usuario(cpf, usuarios)

    if usuario:
        print("Conta criada com sucesso!")
        return {"agencia": agencia, "numero_conta": numero_conta, "usuario":usuario}
    
    print("Usuário não encotrado, por favor cadastre o usuário antes de tentar novamente!")

def main():
    saldo = 800.00
    limite_saque = 3
    agencia = "0001"
    qtd_saques = 0
    extrato = ""
    usuarios = []
    contas = []

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
            criar_usuario(usuarios)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            conta = criar_conta(agencia, numero_conta, usuarios)
            
            if conta:
                contas.append(conta)

        elif opcao == "6":
            print("Encerrando...")
            break

        else:
            print("Operação inválida. Digite novamente o número correspondente a operação que deseja realizar.")

main()