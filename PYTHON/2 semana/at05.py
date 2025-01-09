n1 = input( "Escolha entre Vertebrado ou Invertebrado: ")
n2 = input( "Escolha entre Ave, Inseto, Anelideo ou Mamifero: ")
n3 = input( "Escolha entre Carnivoso, Onivoro, Hematofago ou Herbivoro: ")

if n1 == "Vertebrado":
    if n2 == "Ave":
        if n3 == "Carnivoro":
            print ("Aguia")
        elif n3 == "Onivoro":
            print("Pomba")
        else:
            print("Palavra invalida")
    elif n2 == "Mamifero":
        if n3 == "Onivoro":
         print("Homem")
        elif n3 == "Herbivoro":
            print("Vaca")
        else:
             print("Palavra invalida")
    else:
        print("Palavra invalida")

elif n1 == "Invertebrado":
    if n2 == "Inseto":
        if n3 == "Hematofago":
            print ("Pulga")
        elif n3 == "Herbivoro":
            print("Lagarta")
        else:
            print("Palavra invalida")
    elif n2 == "Anelideo":
        if n3 == "Hematofago":
         print("Sanguessuga")
        elif n3 == "Onivoro":
            print("Minhoca")
        else:
             print("Palavra invalida")
    else:
         print("Palavra invalida")
else:
     print("Palavra invalida")
