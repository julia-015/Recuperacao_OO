from Classes import *

banco = Banco()

def main():
    
    while True:
        try:
            print("+------------------------------+")
            print("| BEM VINDO AO SOFTWARE DO BANCO |")
            print("+------------------------------+")
            print("[1] Criar Conta")
            print("[2] Sacar")
            print("[3] Depositar")
            print("[4] Transferir")
            print("[5] Consultar saldo")
            print("[6] Sair")

            menu = int(input("> "))

            match menu:
                case 1:
                    print("Você está prestes a criar um novo cliente, insira as informações solicitadas.")
                    cliente = criar_cliente()
                    banco.criar_conta(cliente)
                    print("Conta criada com sucesso!")

                case 2:
                    print("Você está prestes a realizar um saque.")
                    sacar(banco)

                case 3:
                    print("Você está prestes a realizar um depósito.")
                    deposito(banco)

                case 4:
                    print("Você está prestes a realizar uma transferência")
                    transferencia(banco)

                case 5:
                    print("Consultar Saldo:")
                    consultar_saldo(banco)

                case 6:
                    break
                    
                case _:
                    print("Opção inválida.")

        except ValueError:
            print('Problema: Digito não correspondente')



def criar_cliente():
    while True:
        nome = input("Digite o nome do cliente: ")
        if nome.isalpha():
            break
        else:
            print("Valor inválido")

    saldo_inicial = input("Digite o saldo inicial do cliente: ")

    cliente = Cliente(nome, saldo_inicial)
    return cliente

def sacar(banco):
    nome = input("Digite o Nome do cliente: ")
    cliente = banco.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do saque: "))
        if valor <= cliente.saldo:
            cliente.saldo -= valor
            print("Saque realizado com sucesso!")
        else:
            print("Saldo insuficiente")

def deposito(banco):
    nome = input("Digite o Nome do cliente: ")
    cliente = banco.buscar_cliente(nome)
    if cliente:
        valor = float(input("Digite o valor do depósito: "))
        cliente.saldo += valor
        print("Depósito realizado com sucesso!")

def transferencia(banco):
    nome_cliente = input("Digite o nome do cliente: ")
    nome_destino = input("Digite o nome do Destinatário: ")
    valor_envio = float(input("Digite o valor a depositar: "))

    cliente_encontrado = banco.buscar_cliente(nome_cliente)
    if cliente_encontrado:
        cliente_destino = banco.buscar_cliente(nome_destino)
        if cliente_destino:
            cliente_encontrado.saldo -= valor_envio
            cliente_destino.saldo += valor_envio
            print(f"Transferência de R${valor_envio:.2f} realizada de {cliente_encontrado.nome} para {cliente_destino.nome}")
        else:
            print("Destinatário não encontrado")
    else:
        print("Remetente não encontrado")

def consultar_saldo(banco):
    nome = input("Digite o Nome do cliente: ")
    cliente = banco.buscar_cliente(nome)
    if cliente:
        print(f"Saldo de {cliente.nome}: R${cliente.saldo:.2f}")