class Funcionarios:
    def __init__(self, nome, salario, cargo):
        self.__nome = nome
        self.__salario = salario
        self.__cargo = cargo
    
    def get_nome(self):
        return self.__nome
    
    def get_salario(self):
        return self.__salario
    
    def get_cargo(self):
        return self.__cargo
    
    def set_nome(self, novonome):
        self.__nome = novonome
    
    def set_salario(self, novosalario):
        self.__salario = novosalario
 
    def set_cargo(self, novocargo):
        self.__cargo = novocargo

class Gerente(Funcionarios):
    def __init__(self, nome, salario, cargo, gerencia, ordena):
        super().__init__(nome, salario, cargo)
        self._gerencia = gerencia
        self._ordena = ordena

    def gerencia(self):
        return f'O gerente está cumprindo sua função de gerenciar!'
    def ordena(self):
        return f'O gerente está dando ordens para os seus subordinados!'
    

class Desenvolvedor (Funcionarios):
    def __init__(self, nome, salario, cargo, desenvolve, obedece):
        super().__init__(nome, salario, cargo)
        self._desenvolve = desenvolve
        self._obedece = obedece

    def desenvolve(self, pauta):
        return f"O desenvolvedor está cumprindo sua função de desenvolver {pauta}"
    def obedece(self):
        return f'O desenvolvedor está obedecendo as ordens dos seus superiores!'
    



Pessoa1=Gerente("Abner", 5000, "Gerente", "Trabalhos", "Funcionários")
Pessoa2=Desenvolvedor("Lucas", 2500, "Desenvolvedor", "Jogos", "Ordens")

print(Pessoa2.desenvolve("Jogos"))