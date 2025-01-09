tam = int(input("Entre com um tamanho"))

vet= []
vetImp= []
vetPar= []

while tam >= 0:
    x = int(input("Entre com um valor"))
    vet.append(x)

    if x%2==0:
        vetPar.append(x)

    else:
        vetImp.append(x)

    tam-=1
    
print(vet)
print(vetImp)
print(vetPar)