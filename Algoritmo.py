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
                    banco.novo_cliente(cliente)
                    print("Conta criada com sucesso!")

                case 2:
                    print("Você está prestes a excluir um cliente, insira as informações solicitadas.")
                    excluir(banco)

                case 3:
                    print("Você está prestes a alterar um cliente")
                    alterar(banco)

                case 4:
                    print("Realizar Transferência")
                    transferencia(banco)

                case 5:
                    print("Realizar depósito")
                    deposito(banco)

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