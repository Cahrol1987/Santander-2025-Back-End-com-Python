from abc import ABC, abstractmethod
from datetime import datetime
import textwrap

class cliente:
    def __init__(self, endereco):
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        transacao.registrar(conta)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class pessoaFisica(cliente):
    def __init__(self, nome, data_nascimento, cpf, endereco):
        super().__init__(endereco)
        self.nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf


class conta:
    def __init__(self, numero, cliente):
        self._saldo = 0
        self._numero = numero
        self._agencia = "0001"
        self._cliente = cliente
        self._historico = historico()

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)
        
    @property
    def saldo(self):
        return self._saldo
        
    @property
    def numero(self):
        return self._numero
        
    @property 
    def agencia(self):
        return self._agencia
        
    @property
    def cliente(self):
        return self._cliente
        
    @property
    def historico(self): 
        return self._historico

    def sacar(self, valor):
        saldo = self.saldo
        excedeu_saldo = valor > saldo

        if excedeu_saldo:
            print("Saldo insuficiente!")
        
        elif valor > 0: 
            self._saldo -= valor
            print("Saque realizado com sucesso!")
            return True
        
        else:
            print("Operação falhou! Valor informado é inválido.")

        return False

    def depositar(self, valor):
        if valor > 0:
            self._saldo += valor
            print("Depósito realizado com sucesso!")
        else: 
            print("Operação falhou! Valor informado é inválido.")
            return False
        
        return True


class contaCorrente(conta):
    def __init__(self, numero, cliente, limite=500, limite_saques=3):
        super().__init__(numero, cliente)
        self.limite = limite
        self.limite_saques = limite_saques

    @classmethod
    def nova_conta(cls, cliente, numero):
        return cls(numero, cliente)

    def sacar(self, valor):
        numero_saques = len([t for t in self.historico.transacoes if t["tipo"] == saque.__name__])
        excedeu_limite = valor > self.limite
        excedeu_saques = numero_saques >= self.limite_saques

        if excedeu_limite:
            print("Operação falhou! O valor informado é maior que o limite.")
        
        elif excedeu_saques:
            print("Operação falhou! Número máximo de saques diários foi excedido.")

        else:
            return super().sacar(valor)
        
        return False
    
    def __str__(self):
        return f"""\nAgência:\t {self.agencia}
C/C:\t\t {self.numero}
Titular:\t {self.cliente.nome}
"""


class historico:
    def __init__(self):
        self._transacoes = []

    @property
    def transacoes(self):
        return self._transacoes
    
    def add_transacao(self, transacao):
        self._transacoes.append(
            {
                "tipo": transacao.__class__.__name__,
                "valor": transacao.valor,
                "data": datetime.now().strftime("%d-%m-%Y %H:%M:%S"),
            }
        )


class transacao(ABC):
    @property
    @abstractmethod
    def valor(self):
        pass

    @abstractmethod
    def registrar(self, conta):
        pass


class saque(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.sacar(self.valor)

        if sucesso_transacao:
            conta.historico.add_transacao(self)


class deposito(transacao):
    def __init__(self, valor):
        self._valor = valor

    @property
    def valor(self):
        return self._valor
    
    def registrar(self, conta):
        sucesso_transacao = conta.depositar(self.valor)

        if sucesso_transacao:
            conta.historico.add_transacao(self)


def menu():
    menu = """
    [1] Depositar
    [2] Sacar
    [3] Extrato
    [4] Criar Usuário
    [5] Criar Conta
    [6] Listar Contas
    [7] Sair
    => """
    return input(f"Digite a opção desejada: \n {menu}")


def validar_usuario(cpf, clientes):
    clientes_filtrados = [cliente for cliente in clientes if cliente.cpf == cpf]
    return clientes_filtrados[0] if clientes_filtrados else None


def recuperar_conta_cliente(cliente):
    if not cliente.contas:
        print("Cliente não possui conta!")
        return
    return cliente.contas[0]


def depositar(clientes):  
    cpf = input("Informe o CPF do cliente: ")
    cliente = validar_usuario(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do depósito: "))
    transacao = deposito(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def sacar(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = validar_usuario(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    valor = float(input("Informe o valor do saque: "))
    transacao = saque(valor)

    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    cliente.realizar_transacao(conta, transacao)


def exibir_extrato(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = validar_usuario(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return
    
    conta = recuperar_conta_cliente(cliente)
    if not conta:
        return
    
    print("EXTRATO")
    transacoes = conta.historico.transacoes

    extrato = ""
    if not transacoes:
        extrato = "Não há movimentações para serem exibidas!"
    else:
        for transacao in transacoes:
            extrato += f"\n{transacao['tipo']}:\n\tR$ {transacao['valor']:.2f}"

    print(extrato)
    print(f"\nSaldo:\n\tR$ {conta.saldo:.2f}")


def criar_cliente(clientes):
    cpf = input("Informe o CPF do cliente: ")
    cliente = validar_usuario(cpf, clientes)

    if cliente:
        print("Já existe cliente cadastrado com esse CPF!")
        return
    
    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento no formato dd-mm-aaaa: ")
    endereco = input("Informe o endereço no formato logradouro, número - bairro - cidade/uf: ")

    cliente = pessoaFisica(nome=nome, data_nascimento=data_nascimento, cpf=cpf, endereco=endereco)
    clientes.append(cliente)

    print("Cliente criado com sucesso!")    


def criar_conta(numero_conta, clientes, contas):
    cpf = input("Informe o CPF do cliente: ")
    cliente = validar_usuario(cpf, clientes)

    if not cliente:
        print("Cliente não encontrado!")
        return

    conta = contaCorrente.nova_conta(cliente=cliente, numero=numero_conta)
    contas.append(conta)
    cliente.contas.append(conta)

    print("Conta criada com sucesso!")    


def listar_contas(contas):
    for conta in contas:
        print("=" * 100)
        print(textwrap.dedent(str(conta)))


def main():
    clientes = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "1":
            depositar(clientes)

        elif opcao == "2": 
            sacar(clientes)
    
        elif opcao == "3":
            exibir_extrato(clientes)
        
        elif opcao == "4":
            criar_cliente(clientes)
        
        elif opcao == "5":
            numero_conta = len(contas) + 1
            criar_conta(numero_conta, clientes, contas)

        elif opcao == "6":
            listar_contas(contas)

        elif opcao == "7":
            print("Encerrando...")
            break

        else:
            print("Operação inválida. Digite novamente o número correspondente a operação que deseja realizar.")


if __name__ == "__main__":
    main()
