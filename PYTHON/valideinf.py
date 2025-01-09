Nome = input("Digite aqui o seu nome: ")
while len(Nome) < 3:
    print ("Nome inválido, insira mais de 3 caracteres!")
    Nome = input("Digite aqui o seu nome: ")

idade = int(input("Digite aqui a sua idade: "))
while (idade< 0 or idade > 150) :
    print ("Idade inválida, insira um numero entre 0 e 150!")
    idade = int(input("Digite aqui a sua idade: "))

Salario = int(input("Digite aqui a sua salario: "))
while Salario <= 0 :
    print ("Salário iyanválido, insira um numero maior que 0!")
    Salario = int(input("Digite aqui a sua idade: "))

Sexo = input("Digite aqui o seu sexo: ")
while Sexo != "F" or Sexo !="M" or Sexo !="Outros" :
    print ("Sexo inválido! Digite uma opção válida!")
    Sexo = input("Digite aqui o seu sexo: ")

EstadoCivil = input("Digite aqui o seu estado civil: ")
while EstadoCivil != "S" or EstadoCivil != "C" or EstadoCivil != "V" or EstadoCivil != "D" :
    print ("Sexo inválido! Digite uma opção válida!")
    EstadoCivil = input("Digite aqui o seu estado civil: ")
