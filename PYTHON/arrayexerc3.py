tam = int(input("Entre com um tamanho"))

vet= []
vetImp= []
vetPar= []

for i in range(tam):
    aux = int(input("Entre com um valor: "))
    vet.append(aux)

    if aux % 2 == 0:
        vetPar.append(aux)

    else:
        vetImp.append(aux)

print(vet)
print(vetImp)
print(vetPar)