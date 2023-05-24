# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame
from config import *

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption('Jogo da velha')

#Cores
cor_amarela = (255, 255, 0)
cor_azul = (0,50,210)
cor_verde = (35,142,35)

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
    window.fill(cor_verde)  # Preenche com a cor verde
    window.blit(titulo1, (100, 110))
    window.blit(titulo2, (180, 165))

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados