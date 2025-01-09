num = int(input("entre com o número: "))

vetor= (1,2,3,4,5,6,7,8,9,9,0,2,2,3,41,1,11)

for i in range (len(vetor)):
    if (num == vetor[i]):
        print (i)
        break

