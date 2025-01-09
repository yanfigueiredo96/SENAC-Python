salario = float(input("Digite o valor do seu salário: "))

if(salario<=280.0):
    reajuste = salario*(20/100) +salario
    aumento = salario*(20/100)
    print("O valor do salário reajustado é:" ,reajuste)
    print("O valor anterior é:" ,salario)
    print("o valor de aumento é 20%")
    print("o valor de aumento foi:" ,aumento)
elif(salario>280.0 and salario<=700.0):
     reajuste = salario*(15/100) +salario
     aumento = salario*(15/100)
     print("O valor do salário reajustado é:" ,reajuste)
     print("O valor anterior é:" ,salario)
     print("o valor de aumento é 15%")
     print("o valor de aumento foi:" ,aumento)

elif(salario>700.0 and salario<1500.0):
     reajuste = salario*(10/100) +salario
     aumento = salario*(10/100)
     print("O valor do salário reajustado é:" ,reajuste)
     print("O valor anterior é:" ,salario)
     print("o valor de aumento é 10%")
     print("o valor de aumento foi:" ,aumento)

elif(salario>=1500):
     reajuste = salario*(5/100) +salario
     aumento = salario*(5/100)
     print("O valor do salário reajustado é:" ,reajuste)
     print("O valor anterior é:" ,salario)
     print("o valor de aumento é 5%")
     print("o valor de aumento foi:" ,aumento)

