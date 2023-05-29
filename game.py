
import pygame
import math
from config import *
from assets import *
 
# Initializing Pygame
pygame.init()

# Initializing window
window = pygame.display.set_mode((1000, 600))
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
click_posicao_x = -1 
click_posicao_y = -1
X_or_O_turn = 'x' # X ou O
end_game = 0 

#Função tabuleiro

def tabuleiro_jogo(window):
    pygame.draw.line(window, BLACK,(205,0),(205,600),10)
    pygame.draw.line(window, BLACK,(405,0),(405,600),10)
    pygame.draw.line(window, BLACK,(0,205),(600,205),10)
    pygame.draw.line(window, BLACK,(0,405),(600,405),10)

def logica_click(click_on_off,click_ult_status,x,y):
    if click[0] == 0 and click_ult_status == 1:
        click_on_off = 1
        x = (math.ceil(mouse[0]/200) - 1)
        y = (math.ceil(mouse[1]/200) - 1)
    if click[0] == 0 and click_ult_status == 0:
        click_on_off = 0
        x = -1
        y = -1
    return click_on_off,click_ult_status,x,y


def draw_celula(window,board_array):
    for n in range(3):
        for nn in range(3):
            if board_array[nn][n] == 'x':
                jogador_x(window,n,nn)
            elif board_array [nn][n] == "o":
                jogador_o(window,n,nn)
            else: 
                pass

def board_array_data(board_array,X_or_O_turn, end_game,x,y):
    if x<3 and y<3:
        if X_or_O_turn == 'x' and board_array[y][x] =='n' and x != -1 and y != -1 and end_game == 0:
            board_array[y][x] == 'x'
            X_or_O_turn = 'o'
        if X_or_O_turn == 'o' and board_array[y][x] =='n' and x != -1 and y != -1 and end_game == 0:
            board_array[y][x] == 'o'
            X_or_O_turn = 'x'
    return board_array,X_or_O_turn

def win_line(window,board_array,end_game,X_or_O_turn):
    if board_array[0][0] == 'x' and board_array[0][1] == 'x' and board_array[0][2] == 'x'\
    or board_array[0][0] == 'o' and board_array[0][1] == 'o' and board_array[0][2] == 'o':
        pygame.draw.line(window,BLACK,(30,100),(570,100),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[1][0] == 'x' and board_array[1][1] == 'x' and board_array[1][2] == 'x'\
    or board_array[1][0] == 'o' and board_array[1][1] == 'o' and board_array[1][2] == 'o':
        pygame.draw.line(window,BLACK,(30,300),(570,300),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[2][0] == 'x' and board_array[2][1] == 'x' and board_array[2][2] == 'x'\
    or board_array[2][0] == 'o' and board_array[2][1] == 'o' and board_array[2][2] == 'o':
        pygame.draw.line(window,BLACK,(30,500),(570,500),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[0][0] == 'x' and board_array[1][0] == 'x' and board_array[2][0] == 'x'\
    or board_array[0][0] == 'o' and board_array[1][0] == 'o' and board_array[2][0] == 'o':
        pygame.draw.line(window,BLACK,(100,30),(100,580),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[0][1] == 'x' and board_array[1][1] == 'x' and board_array[2][1] == 'x'\
    or board_array[0][1] == 'o' and board_array[1][1] == 'o' and board_array[2][1] == 'o':
        pygame.draw.line(window,BLACK,(300,30),(300,580),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[0][2] == 'x' and board_array[1][2] == 'x' and board_array[2][2] == 'x'\
    or board_array[0][2] == 'o' and board_array[1][2] == 'o' and board_array[2][2] == 'o':
        pygame.draw.line(window,BLACK,(500,30),(500,580),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[0][0] == 'x' and board_array[1][1] == 'x' and board_array[2][2] == 'x'\
    or board_array[0][0] == 'o' and board_array[1][1] == 'o' and board_array[2][2] == 'o':
        pygame.draw.line(window,BLACK,(30,30),(580,580),10)
        end_game = 1
        X_or_O_turn = 'x'
    elif board_array[2][0] == 'x' and board_array[1][1] == 'x' and board_array[0][2] == 'x'\
    or board_array[2][0] == 'o' and board_array[1][1] == 'o' and board_array[0][2] == 'o':
        pygame.draw.line(window,BLACK,(580,30),(30,580),10)
        end_game = 1
        X_or_O_turn = 'x'
    return end_game, X_or_O_turn
    
def restart_button(window):
    pygame.draw.rect(window, BLACK, (700,100, 200 , 65))



while True:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    #Variável posição do Mouse
    mouse = pygame.mouse.get_pos()
    mouse_position_x = mouse[0]
    mouse_position_y = mouse[1]
    
    
    #Variável clique do Mouse
    click = pygame.mouse.get_pressed()
    print(click)

    #Jogo
    tabuleiro_jogo(window)
    click_on_off,click_ult_status,click_posicao_x,click_posicao_y = logica_click(click_on_off,click_ult_status,click_posicao_x,click_posicao_y)
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

