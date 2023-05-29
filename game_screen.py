import pygame
from config import *
from assets import *

def game_screen(window):
    # Variável para o ajuste de velocidade
    clock = pygame.time.Clock()

    assets = load_assets()

    DONE = 0
    PLAYING = 1
    state = PLAYING

    
    # Initializing Color
    color = (255,255,255)
    top = 100
    left = 100


    # ===== Loop principal =====
    while state != DONE:
        clock.tick(FPS)

        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                state = DONE

        # ----- Gera saídas
        window.fill(WHITE)  # Preenche com a cor branca

        r1 = pygame.draw.rect(window, color, pygame.Rect(left, top, 120, 100))
        pygame.display.flip()
        r2 = pygame.draw.rect(window, color, pygame.Rect(300, top, 120, 100))
        pygame.display.flip()
        r3 = pygame.draw.rect(window, color, pygame.Rect(500, top, 120, 100))
        pygame.display.flip()
        r4 = pygame.draw.rect(window, color, pygame.Rect(left, 300, 120, 100))
        pygame.display.flip()
        r5 = pygame.draw.rect(window, color, pygame.Rect(300, 300, 120, 100))
        pygame.display.flip()
        r6 = pygame.draw.rect(window, color, pygame.Rect(500, 300, 120, 100))
        pygame.display.flip()
        r7 = pygame.draw.rect(window, color, pygame.Rect(left, 500, 120, 100))
        pygame.display.flip()
        r8 = pygame.draw.rect(window, color, pygame.Rect(300, 500, 120, 100))
        pygame.display.flip()
        r9 = pygame.draw.rect(window, color, pygame.Rect(500, 500, 120, 100))
        pygame.display.flip()


        e = 0
        while e < 9:
            if e == 0 or e%2 == 0:
                r1 = CROCO_IMG
                r2 = CROCO_IMG
                r3= CROCO_IMG
                r4= CROCO_IMG
                r5= CROCO_IMG
                r6= CROCO_IMG
                r7= CROCO_IMG
                r8= CROCO_IMG
                r9= CROCO_IMG
            else:
                r1 = PESSOA_IMG
                r2= PESSOA_IMG
                r3= PESSOA_IMG
                r4= PESSOA_IMG
                r5= PESSOA_IMG
                r6= PESSOA_IMG
                r7= PESSOA_IMG
                r8= PESSOA_IMG
                r9= PESSOA_IMG


        pygame.display.update()  # Mostra o novo frame para o jogador

    return state

window = pygame.display.set_mode((LARGURA,ALTURA))
state = INIT 
while state != QUIT:
    if state == GAME:
        state = game_screen(window)
    else:
        state = QUIT
