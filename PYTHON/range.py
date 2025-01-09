nota = float(input("Entre com uma nota:  "))

while (nota < 0 or nota >  10):
    print("nota inválida!")
    nota = float(input("Entre com uma nota:  "))


print("A nota digitada é" ,nota)