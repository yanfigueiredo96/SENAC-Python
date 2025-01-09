mult=1
soma=0
vetor=[]


for i in range (5):
    x=int(input("Digite o número inteiro: "))
    vetor.append(x)

    soma=soma+vetor[i]
    mult=mult*vetor[i]

print (vetor)
print (mult)
print (soma)