dicionario= {
    "hello" : "olá",
    "hi" : "oi",
    "car" : "carro",
    "teacher" : "professor",
    "bola" : "ball",
    "football" : "futebol",
    "red" : "vermelho",
    "yellow" : "amarelo",
    "table" : "mesa"
}

palavra_inglês=input("Digite uma palavra: ")
if palavra_inglês in dicionario:
    print(f"tradução da palavra {palavra_inglês} é: {dicionario[palavra_inglês]}")