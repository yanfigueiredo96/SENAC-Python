numero = int(input("Digite um número (inteiro e positivo): "))

soma = 0 

for i in range(1, numero +1):
    if numero % i == 0 and i % 2 != 0:
        soma += i 
    
print(f"A soma dos divisores ímpares de {numero} é: {soma}")