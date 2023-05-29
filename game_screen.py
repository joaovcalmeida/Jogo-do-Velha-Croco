import pygame
import math
from config import *
from assets import *
from game import *

class Jogador1(pygame.sprite.Sprite):
   def __init__(self, img, x, y):
       # Construtor da classe mãe (Sprite).
       pygame.sprite.Sprite.__init__(self)

       self.image = img
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

class Jogador2(pygame.sprite.Sprite):
   def __init__(self, img, x, y):
       # Construtor da classe mãe (Sprite).
       pygame.sprite.Sprite.__init__(self)

       self.image = img
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y


def game():
    print("entrou no game screen")
    assets = load_assets()
    window = pygame.display.set_mode((1000, 600))
    window.fill(WHITE)

    #inicializando assets
    background = pygame.image.load('assets/img/6206152.jpg').convert()
    background = pygame.transform.scale(background,(1000,600))


    board_array = [['n', 'n', 'n'],
                ['n', 'n', 'n'],
                ['n', 'n', 'n']]

    #Fontes
    pygame.font.init()
    fonte_t1 = pygame.font.SysFont("goudystout", 42)
    fonte_t2 = pygame.font.SysFont("lucidacalligraphy", 30)
    fonte_t3 = pygame.font.SysFont("Comic Sans MS", 30)

    all_sprites = pygame.sprite.Group()

    #Variavéis Click

    click_ult_status = 0 
    click_on_off = 0
    click_posicao_x = -1 
    click_posicao_y = -1
    X_or_O_turn = 'x' # X ou O
    end_game = 0 

    window.blit(background,(0,0))

    lista = [True] * 9
    i = 0
    while True:
        # ----- Trata eventos
        for event in pygame.event.get():
            # ----- Verifica consequências
            if event.type == pygame.QUIT:
                return QUIT
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:

                x_mouse = event.pos[0]
                y_mouse = event.pos[1]
                # Criando o jogador1 na posição x = 10 y = 10
            
                #pygame.draw.line(window, BLACK,(205,0),(205,600),10)
                if lista[0] == True and x_mouse < 205 and y_mouse < 205:
                    x = 0
                    y = 0
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista [0] = False

                if lista[1] == True and  205 < x_mouse < 425 and y_mouse < 205:
                    x = 215
                    y = 0
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[1] = False
                
                if lista[2] == True and x_mouse > 425 and y_mouse < 205:
                    x = 426
                    y = 0
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[2] = False

                if lista[3] == True and x_mouse < 205 and 425 > y_mouse > 205:
                    x = 0
                    y = 216
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[3] = False
                
                if lista[4] == True and 205 < x_mouse < 425 and 425 > y_mouse > 205:
                    x = 216
                    y = 216
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[4] = False
                
                if lista[5] == True and x_mouse > 425 and 425 > y_mouse > 205:
                    x = 425
                    y = 216
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[5] = False
                
                if lista[6] == True and x_mouse < 205 and y_mouse > 425:
                    x = 0
                    y = 425
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[6] = False
                
                if lista[7] == True and 205 < x_mouse < 425 and y_mouse > 425:
                    x = 216
                    y = 425
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[7] = False

                if lista[8] == True and x_mouse > 425 and y_mouse > 425:
                    x = 425
                    y = 425
                    jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                    jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                    if i ==0 or i % 2 == 0 :
                        all_sprites.add(jogador1)
                    else: 
                        all_sprites.add(jogador2)
                    i+=1
                    lista[8] = False

                
                
        
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
        restart_game(board_array,click_posicao_x,click_posicao_y,end_game,click_on_off)

        #Clique último status

        if click[0] == 1:
            click_ult_status = 1 
        else:
            click_ult_status = 0 

        #desenhando o jogador1
        all_sprites.draw(window)
        pygame.display.update()