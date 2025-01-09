import random

# Função para simular o lançamento de um dado
def lançar_dado():
    return random.randint(1, 6)

# Função principal
def simular_lançamentos():
    # Criando um vetor de contadores para os números de 1 a 6
    contadores = [0] * 6  # Índices de 0 a 5 representam os números de 1 a 6
    
    # Lançando o dado 100 vezes
    for _ in range(100):
        resultado = lançar_dado()
        contadores[resultado - 1] += 1  # Incrementa o contador do número sorteado
    
    # Exibindo os resultados
    for i in range(6):
        print(f'O número {i + 1} apareceu {contadores[i]} vezes.')

# Executando o programa
simular_lançamentos()