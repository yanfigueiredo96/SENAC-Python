class Animal:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self):
        return ("Subclasses devem implementar este método")
    
class Cachorro(Animal):
    def __init__(self, nome, idade, tamanho_porte, andar, comer):
        super().__init__(nome, idade)
        self.tamanho_porte = tamanho_porte
        self.andar = andar
        self.comer = comer
    def falar(self):
        return f'au au!'
    
rex = Cachorro("Rex", 11, "Vira-Lata")
print (rex.falar())