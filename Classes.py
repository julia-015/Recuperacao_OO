class Cliente:
    def __init__(self, nome, saldo_inicial):
        self.nome = nome
        self.saldo_inicial = saldo_inicial

    def getCliente(self):
        return self.nome, self.saldo_inicial

    def setNome(self, x):
        self.nome = x

    def setSaldo_Inicial(self, x):
        self.saldo_inicial = x

class Banco():

    def __init__(self):
        self._clientes = {}

    def criar_conta(self, cliente):
        self._clientes[cliente.nome] = cliente
        print(f"{cliente.nome} foi adicionado")

class Transferencia():

    def sacar(self, conta, valor):
        pass

    def depositar(self, conta, valor):
        pass

    def transferir(self, origem, destino, valor):
        pass
    
    def saldo(self, conta):
        pass