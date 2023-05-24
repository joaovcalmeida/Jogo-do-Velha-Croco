import pygame
 
# Initializing Pygame
pygame.init()

# Initializing surface
surface = pygame.display.set_mode((800,600))
    # Initializing Color
color = (255,255,255)
top = 100
left = 100
game = True

while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT:
            game = False  
    r1 = pygame.draw.rect(surface, color, pygame.Rect(left, top, 120, 100))
    pygame.display.flip()
    r2 = pygame.draw.rect(surface, color, pygame.Rect(300, top, 120, 100))
    pygame.display.flip()
    r3 = pygame.draw.rect(surface, color, pygame.Rect(500, top, 120, 100))
    pygame.display.flip()
    r4 = pygame.draw.rect(surface, color, pygame.Rect(left, 300, 120, 100))
    pygame.display.flip()
    r5 = pygame.draw.rect(surface, color, pygame.Rect(300, 300, 120, 100))
    pygame.display.flip()
    r6 = pygame.draw.rect(surface, color, pygame.Rect(500, 300, 120, 100))
    pygame.display.flip()
    r7 = pygame.draw.rect(surface, color, pygame.Rect(left, 500, 120, 100))
    pygame.display.flip()
    r8 = pygame.draw.rect(surface, color, pygame.Rect(300, 500, 120, 100))
    pygame.display.flip()
    r9 = pygame.draw.rect(surface, color, pygame.Rect(500, 500, 120, 100))
    pygame.display.flip()
    

