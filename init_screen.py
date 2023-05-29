# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *
from sprites import *
from assets import *

# ----- Gera tela principal
#window = pygame.display.set_mode((LARGURA, ALTURA))

def init_screen(window):

    all_buttons = pygame.sprite.Group()
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()
    assets = load_assets()

    play = Botao(assets, 'Play')
    all_buttons.add(play)
    # ----- Inicia estruturas de dados
    game = True

    # ----- Inicia assets
    fonte_t1 = pygame.font.SysFont("goudystout", 48)
    fonte_t2 = pygame.font.SysFont("lucidacalligraphy", 30)

    titulo1 = fonte_t1.render('Jogo da Velha', True, (255, 255, 255))
    titulo2 = fonte_t2.render('Distribuição CrocoRichards', True, (255, 255, 255))

    # ===== Loop principal =====
    while game:
        # Ajusta a velocidade do jogo.
        clock.tick(FPS)
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                game = False
                state = QUIT
                game = False

            if event.type == pygame.KEYUP:
                    state = GAME
                    game = False
                
            if event.type == pygame.MOUSEBUTTONDOWN:
                    if play.rect.collidepoint(event.pos):
                        state = GAME
                        game = False

            if event.type == pygame.MOUSEMOTION:
                    #Alterando cor do botão
                    if play.rect.collidepoint(event.pos):
                        play.mouse_over(True)
                    else:
                        play.mouse_over(False)

        # ----- Gera saídas
        window.fill(GREEN)  # Preenche com a cor verde
        window.blit(titulo1, (52, 110))
        window.blit(titulo2, (180, 165))
        window.blit(play.image, play.rect)
        all_buttons.draw(window)
        # ----- Atualiza estado do jogo
        pygame.display.update()  # Mostra o novo frame para o jogador
        
    return state