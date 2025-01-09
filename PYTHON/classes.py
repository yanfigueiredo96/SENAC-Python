class Animal:
    def __init__(self, c, tmn, name):  #__init___ é usado para construir 
        self.cor = c
        self.tamanho = tmn
        self.nome = name

    def set_cor(self, c):
        self.cor = c
    
    def set_tamanho(self, t):
        self.tamanho = t

    def set_nome(self, n):
        self.nome = n

    def get_cor(self):
        print(self.cor)
    def get_tamanho(self):
        print(self.tamanho)
    def get_nome(self):
        print(self.nome)


    def respiração():
        print("Estou respirando!")
    def emissão_som():
        print("glub glub glub!")
    def locomoção():
        print("Nadando...")
    
baleia = Animal ("azul", 1000, "willy")
cachorro = Animal ("caramelo", 50, "caramelo")
gato = Animal ("branco", 40, "félix")
urubu = Animal ("preto", 30, "dupix")
jacaré = Animal ("verde", 60, "Dante")
humano = Animal ("negro", 100, "Yan")

gato.get_cor()
gato.set_cor("Azul")
gato.get_cor()