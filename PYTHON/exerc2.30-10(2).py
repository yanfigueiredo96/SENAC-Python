idade = []
altura = []

for i in range(2):
    id= int(input("Digite a idade: "))
    alt= float(input("Digite a altura: "))

    idade.append(id)
    altura.append(alt)

idade.reverse()
altura.reverse()

print (idade)
print (altura)