vetor1 = []
vetor2 = []
vetor3 = []
for i in range(5):
    x = input("Digite aqui o nome: ")
    vetor1.append(x)

for i in range(5):
    y = int(input("Digite aqui o valor: "))
    vetor2.append(y)

for i in range(5):
        vetor3.append(vetor1[i])
        vetor3.append(vetor2[i])

print(vetor3)