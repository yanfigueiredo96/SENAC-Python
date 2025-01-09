n1=int(input("Digite um numero:"))
operador= input("Digite uma operação matemática:")
n2=int(input("Digite outro numero:"))

if operador == "+":
    resultado = n1 + n2
    print(" O resultado é:", n1, "+" ,n2, "=", resultado)
elif operador == "-":
    resultado = n1 - n2
    print(" O resultado é:", n1, "-" ,n2, "=", resultado)
elif operador == "*":
    resultado = n1 * n2
    print(" O resultado é:", n1, "*" ,n2, "=", resultado)
elif operador == "/":
    if n2 == 0:
        print("Não é possivel dividir por zero!")
    else:
     resultado = n1 / n2
     print(" O resultado é:", n1, "/" ,n2, "=", resultado)
    
else:
    print("Erro: Operador inválido!")