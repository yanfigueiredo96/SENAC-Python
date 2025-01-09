N = int(input("Digite a quantidade de alunos: "))

aprovados=0

for i in range (N):
    
    nota1 = float(input("Digite o valor da primeira nota aqui: "))
    nota2 = float(input("Digite o valor da segunda nota aqui: "))
    nota3 = float(input("Digite o valor da terceira nota aqui: "))

    media = (nota1 + nota2 + nota3) / 3
    if media >= 5.0:
        aprovados+=1
        
porcentagem_aprovados = (aprovados/N) *100
print (f"{porcentagem_aprovados}")

