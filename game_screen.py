import pygame
import math
from config import *
from assets import *
from game import *


def game():
    print("entrou no game screen")
    window = pygame.display.set_mode((1000, 600))
    window.fill(WHITE)


    board_array = [['n', 'n', 'n'],
                ['n', 'n', 'n'],
                ['n', 'n', 'n']]

    #Fontes
    pygame.font.init()
    fonte_t1 = pygame.font.SysFont("goudystout", 42)
    fonte_t2 = pygame.font.SysFont("lucidacalligraphy", 30)
    fonte_t3 = pygame.font.SysFont("Comic Sans MS", 30)

    #Variavéis Click

    click_ult_status = 0 
    click_on_off = 0
    click_posicao_x = -1 
    click_posicao_y = -1
    X_or_O_turn = 'x' # X ou O
    end_game = 0 

    
    while True:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                return QUIT
                pygame.quit()
                quit()
        
        #Variável posição do Mouse
        mouse = pygame.mouse.get_pos()
        mouse_position_x = mouse[0]
        mouse_position_y = mouse[1]
        
        
        #Variável clique do Mouse
        click = pygame.mouse.get_pressed()
    
        #Jogo
        tabuleiro_jogo(window)
        click_on_off,click_ult_status,click_posicao_x,click_posicao_y = logica_click(click,mouse,click_on_off,click_ult_status,click_posicao_x,click_posicao_y)
        draw_celula(window,board_array)
        board_array,X_or_O_turn = board_array_data(board_array,X_or_O_turn, end_game,click_posicao_x,click_posicao_y)
        end_game, X_or_O_turn = win_line(window,board_array,end_game,X_or_O_turn)
        restart_button(window)

        #Clique último status

        if click[0] == 1:
            click_ult_status = 1 
        else:
            click_ult_status = 0 

        pygame.display.update()