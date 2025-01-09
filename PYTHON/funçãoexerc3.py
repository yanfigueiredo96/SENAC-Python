# def func2(n):
#     aux = 0 
#     i = 1

#     for i in range(n+1):

#         aux=1
#         print ((str(aux)+" ")*i)
#         aux+=1

#         for j in range(n+1):
#             print ((str(aux), end="")
# func2(10)

def forfor (n):
    for i in range (n+1):
        for j in range (i+1):
            print(j, end=" ")
        print ()

forfor(10)