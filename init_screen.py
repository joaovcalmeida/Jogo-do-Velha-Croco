# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from sprites import *
from assets import *

# ----- Gera tela principal
#window = pygame.display.set_mode((LARGURA, ALTURA))

def init_screen(window):
    pygame.init()

    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    btn = Botao(assets,'')

    # ----- Gera tela principal
    pygame.display.set_caption('Jogo da velha')

    medidas_botao = Botao(assets, '')

    # ----- Inicia estruturas de dados
    game = True


    # ----- Inicia assets
    fonte_t1 = pygame.font.SysFont("goudystout", 42)
    fonte_t2 = pygame.font.SysFont("lucidacalligraphy", 30)

    titulo1 = fonte_t1.render('Jogo da Velha', True, (255, 255, 255))
    titulo2 = fonte_t2.render('Distribuição CrocoRichards', True, (255, 255, 255))

    # ===== Loop principal =====
    while game:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False

        # ----- Gera saídas
        window.fill(GREEN)  # Preenche com a cor verde
        window.blit(titulo1, (100, 110))
        window.blit(titulo2, (180, 165))

        # Ajusta a velocidade do jogo.
        clock.tick(FPS)

        # Processa os eventos (mouse, teclado, botão, etc).
            # Verifica se foi fechado.
        if event.type == pygame.QUIT:
                state = QUIT
                running = False

        if event.type == pygame.KEYUP:
                state = GAME
                running = False
            
        if event.type == pygame.MOUSEBUTTONDOWN:
                state = GAME
                running = False

        if event.type == pygame.MOUSEMOTION:
                #Alterando cor do botão

            if btn.rect.collidepoint(event.pos):
                btn.mouse_over(True)
            else:
                btn.mouse_over(False)
    
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador

        return state