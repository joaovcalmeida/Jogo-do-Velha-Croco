
import pygame
import math
from config import *
from assets import *
 
# Initializing Pygame
pygame.init()

# Initializing window
window = pygame.display.set_mode((LARGURA, ALTURA))
window.fill(WHITE)


board_array = [['n', 'n', 'n'],
               ['n', 'n', 'n'],
               ['n', 'n', 'n']]

#Fontes
pygame.font.init()
fonte_t1 = pygame.font.SysFont("goudystout", 42)
fonte_t2 = pygame.font.SysFont("lucidacalligraphy", 30)

#Variavéis Click

click_ult_status = 0 
click_on_off = 0
click_posicao_x = 1 
click_posicao_y = 1
O_or_X = 'x' # X ou O
end_game = 0 

#Função tabuleiro

def tabuleiro_jogo(window):
    pygame.draw.line(window, BLACK,(170,0),(170,600),10)
    pygame.draw.line(window, BLACK,(370,0),(370,600),10)
    pygame.draw.line(window, BLACK,(0,190),(550,190),10)
    pygame.draw.line(window, BLACK,(0,390),(550,390),10)

def logica_clique(click_on_off,click_ult_status,x,y):
    if clique[0] == 0 and click_ult_status == 1:
        click_on_off = 1
        x = (math.ceil(mouse[0]/200) - 1)
        y = (math.ceil(mouse[1]/200) - 1)
    if clique[0] == 0 and click_ult_status == 0:
        click_on_off = 0
        x = -1
        y = -1
    return click_on_off,click_ult_status,x,y


def draw_celula(window,board_array):
    

game = True

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False  
    
    tabuleiro_jogo(window)
    click_on_off,click_ult_status,click_posicao_x,click_posicao_y = logica_clique(click_on_off,click_ult_status,click_posicao_x,click_posicao_y)

    #Variável posição do Mouse
    mouse = pygame.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]


    #Variável clique do Mouse
    clique = pygame.mouse.get_pressed()


    #Clique último status

    if clique[0] == 1:
        click_ult_status = 1 
    else:
        click_ult_status = 0 

    pygame.display.update()

