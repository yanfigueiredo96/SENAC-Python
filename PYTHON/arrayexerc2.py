lista = []


for i in range(10):
    aux = int(input("Entre com um valor: "))
    lista.append(aux)

print("Os valores em ordem reversa foram: ")
for i in range(9, -1, -1):  
    print(lista[i])
