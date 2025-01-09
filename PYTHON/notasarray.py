vet= []

ct1 = 0
ct2 = 0

for i in range (2):
    nota1 = float(input("Digite sua primeira nota aqui: "))
    nota2 = float(input("Digite sua segunda nota aqui: "))
    nota3 = float(input("Digite sua terceira nota aqui: "))
    nota4 = float(input("Digite sua quarta nota aqui: "))


    media= (nota1 + nota2 + nota3 + nota4) /4

    vet.append(media)
for  i in range (2):
    if vet[i]>=7.0:
        ct1 +=1
    else:
        ct2 +=1
print("Aprovados: " ,ct1)
print("Reprovados: " ,ct2)

