import pygame

pygame.init()

tamanho_tela= (800 , 800)
tela = pygame.display.set_mode(tamanho_tela)
pygame.display.set_caption("Da fama ao sucesso")

tamanho_bola = 15
bola = pygame.Rect(100,500,tamanho_bola, tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0,750, 100, 15)

quantidade_blocos_linhas = 8
quantidade_linhas_blocos = 10 
quantidade_total_blocos = quantidade_blocos_linhas * quantidade_linhas_blocos

def criar_blocos(quantidade_blocos_linhas,quantidade_linhas_blocos):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_blocos = 5 
    largura_bloco = largura_tela / 8 - distancia_blocos
    altura_bloco = 15
    distancia_entre_lihas = altura_bloco + 10
    blocos = []
    for j in range (quantidade_linhas_blocos):
        for i in range(quantidade_blocos_linhas):
            bloco = pygame.Rect(i * (largura_bloco + distancia_blocos),j * distancia_entre_lihas,largura_bloco,altura_bloco)
            blocos.append(bloco)
    return blocos

cores = {
    "branca": (255,255,255) ,
    "preta": (0,0,0) ,
    "amarela": (255,255,0) ,
    "azul": (0,0,255),
    "verde":(0,255,0)
}

fim_jogo = False
pontuacao = 0 
movimento_bola = [1,-1]

#desenhar as coisas na tela!
def desenhar_inicio_jogo():
    tela.fill(cores["preta"])
    pygame.draw.rect(tela, cores["azul"],jogador )
    pygame.draw.rect(tela, cores["branca"],bola )

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela, cores["amarela"],bloco)

def movimentar_jogador(evento):
    if evento.type == pygame.KEYDOWN:
        if evento.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
                jogador.x = jogador.x + 5
        if evento.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - 5

def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]
    if bola.y <=0:
        movimento[1] = - movimento[1]
    if bola.x + tamanho_bola >= tamanho_tela[0]:
        movimento[0] = - movimento[0]
    if bola.y + tamanho_bola >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x,bola.y):
        movimento[1] = - movimento[1]
    for bloco in blocos:
        if bloco.collidepoint(bola.x, bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1] 

    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None,30)
    texto = fonte.render(f"Pontuação: {pontuacao}", 1, cores["amarela"])
    tela.blit(texto, (0,780))
    if pontuacao >= quantidade_total_blocos:
        return True
    else: 
        return False




blocos = criar_blocos(quantidade_blocos_linhas, quantidade_linhas_blocos)


while not fim_jogo:
    desenhar_inicio_jogo()
    desenhar_blocos(blocos)
    fim_jogo = atualizar_pontuacao(quantidade_total_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            fim_jogo = True
    
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
        fim_jogo = True
    pygame.time.wait(1)
    pygame.display.flip()

pygame.quit()