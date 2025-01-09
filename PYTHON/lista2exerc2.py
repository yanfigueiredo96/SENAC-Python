soma= 0 
contagem = 0

while True:
    numero = int(input("Digite um número inteiro: "))

    if numero < 0:
        break

    soma += numero
    contagem += 1

if contagem > 0:
    media = soma / contagem 

    if int(media) % 2 == 0:
        print (f"A media dos números digitados é {media} e é par.")

    
    else:
        print (f"A media dos números digitados é {media} e é ímpar.")