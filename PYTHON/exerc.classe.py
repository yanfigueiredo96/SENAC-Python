class Produto:
    def __init__(self, nome,preco,quantidade):
        self.nome = nome
        self.preço = preco
        self.quantidade = quantidade

    def set_nome(self, n):
        self.nome = n
    
    def set_preço(self, p):
        self.preço = p

    def set_quantidade(self, qnt):
        self.quantidade = qnt

    def get_nome(self):
        print(self.nome)
    def get_preço(self):
        print(self.preço)
    def get_quantidade(self):
        print(self.quantidade)

item1 = Produto("blusa", 50, 7)
item2 = Produto("calça", 100, 13)
item3 = Produto("Short", 30, 10)

def desconto(self):
    prec_desc = (self.preço) * desc /100 
    return prec_desc

def total(self):
    total = self.preço * qnt
    return total