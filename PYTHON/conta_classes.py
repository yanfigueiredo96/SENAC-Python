class Conta:
    def __init__(self, saldo, nome):
        self.__saldo = saldo # "__" é usado para criar uma classe privada que só pode ser vista usando o get
        self.nome = nome
    def get_saldo(self):
        return self.__saldo
    def get_deposito(self, valor):
        self.__saldo += valor
        return self.__saldo
    def get_saque(self, valor):
        self.__saldo -= valor
        return self.__saldo

c1 = Conta(1000,"José")
print(c1.get_deposito(200))
print(c1.get_saque(444))