n1 = float(input("número: "))
n2 = float(input("número: "))
n3 = float(input("número: "))

if(n1>n2 and n2>n3):
    print(n1, "maior")
    if (n2>n3):
        print(n2, "do meio")
        print(n3, "menor")
        
    
if(n2>n1 and n1>n3):
    print(n2, "maior")
    if(n1>n3):
         print(n1, "do meio")
         print(n3, "menor" )

if(n3>n1 and n1>n2):
    print(n3, "maior")
    if (n1>n2):
        print(n1,"do meio")
        print(n2, "menor")
        