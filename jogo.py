# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
import random
from config import *
from init_screen import *
from game import *
from game_screen import *



pygame.init()
pygame.mixer.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da Velha Croco')

state = INIT


while state != QUIT:
    if state == INIT:
        state = init_screen(window)
    elif state == GAME:
        state = game()
    else:
        state = QUIT

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

