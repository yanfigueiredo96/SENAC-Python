idade = []
altura = []

for i in range(5):
    x = int(input("Digite aqui a sua idade: "))
    idade.append(x)

for i in range(5):
    y = float(input("Digite aqui a sua altura: "))
    altura.append(y)

print("Idades em ordem reversa:", list(reversed(idade)))
print("Alturas em ordem reversa:", list(reversed(altura)))
