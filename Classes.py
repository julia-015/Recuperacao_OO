class Cliente:
    def __init__(self, nome, saldo=0):
        self.nome = nome
        self.saldo = saldo

    def getCliente(self):
        return self.nome, self.saldo_inicial

    def setNome(self, x):
        self.nome = x

class Banco():

    def __init__(self):
        self._clientes = {}

    def criar_conta(self, cliente):
        conta = 0000
        self._clientes[cliente.nome] = cliente
        print(f"{cliente.nome} foi adicionado")
        ContaCriada = conta +  1
        return ContaCriada
    
    def buscar_cliente(self, nome):
        return self._clientes.get(nome, None)

class Transferencia():

    def __init__(self, cliente, saldo):
        self._cliente = cliente
        self._saldo = saldo
        self._enviado = 0
        self._recebido = 0

    def sacar(self, valor):
        if valor <= self._saldo:
            self._saldo -= valor
            self._enviado += valor
        else:
            print("Saldo Insuficiente")

    def deposito(self, valor):
        self._saldo += valor
        self._recebido += valor

    def detalhes(self):
        print(f'Cliente: {self._cliente.nome}\nSaldo: {self._saldo}')
        if self._enviado > 0:
            print(f"Sua transferência foi enviada! - {self._enviado}")
        if self._recebido > 0:
            print(f"Sua transferência foi recebida! - {self._recebido}")
        print()
    