saque = int(input("Digite o valor desejado para o saque: "))
if 10 <= saque <= 100:
    notas_100 = saque // 100
    saque = saque % 100

    notas_50 = saque // 50
    saque = saque % 50
    
    notas_10 = saque // 10
    saque = saque % 10
    
    notas_5 = saque // 5
    saque = saque % 5
    
    notas_1 = saque // 1
    saque = saque % 1
    
    print(f"Notas de:" [notas_100])
    print(f"Notas de:" [notas_50])
    print(f"Notas de:" [notas_10])
    print(f"Notas de:" [notas_5])
    print(f"Notas de:" [notas_1])