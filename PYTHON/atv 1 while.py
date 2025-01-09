usuario = input("Digite o nome de usuário: ")
senha = input("Digite a sua senha: ")

while (usuario == senha):
    print("Usuário e senha não podem ser iguais! tente novamente!")
    senha = input("Digite a sua senha: ")