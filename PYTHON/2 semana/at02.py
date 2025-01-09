salario = float(input('Digite seu salario atual:'))
plano =input('Digite o seu plano(A,B ou C):')
if plano == "A":
    novo_salario = salario * 1.10
elif plano == "B":
    novo_salario = salario *1.15
elif plano == "C":
    novo_salario = salario *1.20
else:
    print ("Plano invalido!")
    novo_salario = salario
print ('O novo salario é: R$', novo_salario)