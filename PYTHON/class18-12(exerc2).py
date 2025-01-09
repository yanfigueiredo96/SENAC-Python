class Transportes:
    def __init__(self, modelo, nome):
        self.modelo = modelo
        self.nome = nome
    
    def locomocao(self):
        return f'O veículo faz o barulho'

class Carro(Transportes):
    def __init__(self, modelo, nome, locomocao):
        super().__init__(modelo, nome)
        

    def locomocao (self):
        return f'VVVVVRRRRRUUUUUMMMMMMM'

class Moto(Transportes):
    def __init__(self, modelo, nome, locomocao):
        super().__init__(modelo, nome)

    
    def locomocao (self):
        return f'VVVVVRRRRRIIIIIIMMMMMM'
    
class Barco(Transportes):
    def __init__(self, modelo, nome, locomocao):
        super().__init__(modelo, nome)

    def locomocao (self):
        return f'POOOOOOOOOOOOOOOOOM'
    
class Avião(Transportes):
    def __init__(self, modelo, nome, locomocao):
        super().__init__(modelo, nome)

    def locomocao (self):
        return f'ZUUUUUUUUUUUUUUUUM'

carro1 = Carro("Ford", "Ká", "estrada") 
moto1 = Moto("Honda", "CG125", "duas rodas")
barco1 = Barco("Iate", "DO NEYMAR", "Por mar")
avião1= Avião("Boing", "777", "por ar")

print (carro1.locomocao())
print (moto1.locomocao())
print (barco1.locomocao())
print (avião1.locomocao())
