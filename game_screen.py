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

class vencedorx(pygame.sprite.Sprite):
   def __init__(self, img, x, y):
       # Construtor da classe mãe (Sprite).
       pygame.sprite.Sprite.__init__(self)

       self.image = img
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

class vencedoro(pygame.sprite.Sprite):
   def __init__(self, img, x, y):
       # Construtor da classe mãe (Sprite).
       pygame.sprite.Sprite.__init__(self)

       self.image = img
       self.rect = self.image.get_rect()
       self.rect.x = x
       self.rect.y = y

class Velha(pygame.sprite.Sprite):
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
    j=0
    jogando = True
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

                if 700<=x_mouse<= 900 and 100<=y_mouse<=165:
                     return GAME
                # Criando o jogador1 na posição x = 10 y = 10
            
                #pygame.draw.line(window, BLACK,(205,0),(205,600),10)
                if jogando == True:
                    music = True
                    if lista[0] == True and x_mouse < 205 and y_mouse < 205:
                        x = 5
                        y = 0
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                            all_sprites.add(jogador1)
                            board_array [0][0] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [0][0] = 'o'
                        i+=1
                        lista [0] = False

                    if lista[1] == True and  205 < x_mouse < 425 and y_mouse < 205:
                        x = 210
                        y = 0
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [0][1] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [0][1] = 'o'
                        i+=1
                        lista[1] = False
                    
                    if lista[2] == True and x_mouse > 425 and x_mouse < 620 and y_mouse < 205:
                        x = 415
                        y = 0
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [0][2] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [0][2] = 'o'
                        i+=1
                        lista[2] = False

                    if lista[3] == True and x_mouse < 205 and 425 > y_mouse > 205:
                        x = 5
                        y = 205
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [1][0] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [1][0] = 'o'
                        i+=1
                        lista[3] = False
                    
                    if lista[4] == True and 205 < x_mouse < 425 and 425 > y_mouse > 205:
                        x = 210
                        y = 205
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [1][1] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [1][1] = 'o'
                        i+=1
                        lista[4] = False
                    
                    if lista[5] == True and x_mouse > 425 and x_mouse<620 and 425 > y_mouse and y_mouse > 205:
                        x = 415
                        y = 205
                        jogador1 = Jogador1(assets[CROCO_IMG], x,y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [1][2] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [1][2] = 'o'
                        i+=1
                        lista[5] = False
                    
                    if lista[6] == True and x_mouse < 205 and y_mouse > 425:
                        x = 5
                        y = 405
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [2][0] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [2][0] = 'o'
                        i+=1
                        lista[6] = False
                    
                    if lista[7] == True and 205 < x_mouse and x_mouse < 425 and y_mouse > 425:
                        x = 210
                        y = 405
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [2][1] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [2][1] = 'o'
                        i+=1
                        lista[7] = False

                    if lista[8] == True and x_mouse > 425 and x_mouse <620 and y_mouse > 425:
                        x = 415
                        y = 405
                        jogador1 = Jogador1(assets[CROCO_IMG], x, y)
                        jogador2 = Jogador2(assets[PESSOA_IMG],x,y)
                        if i ==0 or i % 2 == 0 :
                                all_sprites.add(jogador1)
                                board_array [2][2] = 'x'
                        else: 
                            all_sprites.add(jogador2)
                            board_array [2][2] = 'o'
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
        # draw_celula(window,board_array)
        board_array,X_or_O_turn = board_array_data(board_array,X_or_O_turn, end_game,click_posicao_x,click_posicao_y)
        all_sprites.draw(window) #desenhando o jogador1
        end_game, X_or_O_turn = win_line(window,board_array,end_game,X_or_O_turn)
        if end_game == 1:
            jogando = False
        restart_button(window)
        restart_game(board_array,click_posicao_x,click_posicao_y,end_game,click_on_off)

        

        if jogando == False:
            vencedor = verifica_jogo_da_velha(board_array)
            if vencedor == 'Croco Venceu':
                 x= 650
                 y = 350
                 croco = vencedorx(assets[CROCO_VENCEU],x,y)
                 all_sprites.add(croco)
                 if music == True:
                    assets['croco_sound'].play()
                    music = False
            else:
                 x= 615
                 y = 350
                 novelli = vencedoro(assets[DJ_VENCEU],x,y)
                 all_sprites.add(novelli)
                 if music == True:
                      assets['dj_sound'].play()
                      music = False

            

        elif lista == [False] * 9:
            x= 650
            y = 350
            velha = Velha(assets[DEU_VELHA],x,y)
            all_sprites.add(velha)

        #Clique último status

        if click[0] == 1:
            click_ult_status = 1 
        else:
            click_ult_status = 0 

        
        pygame.display.update()