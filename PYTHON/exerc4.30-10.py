idade = []
altura =[]
contador= 0
soma=0
media = 0 

for i in range(3):
    id=int(input("Digite a idade do aluno: "))
    alt=float(input("Digite a altura do aluno: "))
    
    idade.append(id)
    altura.append(alt)
    
for i in range (3):
    soma += altura[i]

  
media=soma/len(altura)

for i in range (len(idade)):
    if (idade[i] >= 13) and (altura[i]<media):
        contador+=1


print (contador)

