class Carro:   # ENCAPSULAMENTO (ESCONDER DO USUÁRIO)
    def __init__(self, modelo, velocidade):
        self.__modelo = modelo
        self.__velocidade = velocidade
        

    def get_modelo (self):
        ''' Método para retornar o valor do modelo'''
        return self.__modelo

    def get_velocidade (self):
        '''Método para retornar o valor da velocidade'''
        return self.__velocidade
    
    

    def acelerar(self, valor):
        self.__velocidade += valor
        return self.__velocidade
    

    def desacelerar(self,valor):
        if self.__velocidade > 0:
            self.__velocidade -= valor
            return self.__velocidade
        
        else: 
            print ("O carro está parado!")