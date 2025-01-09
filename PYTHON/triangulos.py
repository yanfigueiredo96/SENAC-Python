Lado1 = float(input("Digite o valor do lado: "))
Lado2 = float(input("Digite o valor do lado: "))
Lado3 = float(input("Digite o valor do lado: "))


if (Lado1 + Lado2 >= Lado3) and (Lado1 + Lado3 >= Lado2) and (Lado2 + Lado3 >= Lado1):

    if  Lado1 == Lado2 == Lado3:
        print ("O triângulo é equilátero!")

    elif Lado1 == Lado2 or Lado1 == Lado3 or Lado2 == Lado3:
        print ("O triângulo é Isóceles!")

    elif Lado1 % Lado2 or Lado1 % Lado3 or Lado2 % Lado3:
        print ("O triângulo é Escaleno!")

else:
    print("Não é triêngulo, tente novamente!")