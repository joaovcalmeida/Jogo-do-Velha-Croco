import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
CROCO_IMG = 'croco_img'
PESSOA_IMG = 'pessoa_img'
CROCO_SOUND = 'croco_sound'
DJ_SOUND = 'dj_sound'
RIVER_SOUND ='river_sound'
WIN_SOUND = 'win_sound'





def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,'')).convert()
    assets[CROCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, '')).convert_alpha()
    assets[PESSOA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'')).convert_alpha()

# Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, ''))
    pygame.mixer.music.set_volume(0.4)
    assets[DJ_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[RIVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[WIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets



# Jogo-do-Velha-Croco


# ----- Inicia assets
CROCODILO_WIDTH = 50
CROCODILO_HEIGHT = 38
PESSOA_WIDTH = 50
PESSOA_HEIGHT = 38

assets={}
assets['background'] = pygame.image.load('assets/img/').convert()
assets['crocodilo_img'] = pygame.image.load('assets/img/').convert_alpha()
assets['pessoa_img'] = pygame.transform.scale(assets['pessoa_img'], (METEOR_WIDTH, METEOR_HEIGHT))
assets['ship_img'] = pygame.image.load('assets/img/playerShip1_orange.png').convert_alpha()
assets['ship_img'] = pygame.transform.scale(assets['ship_img'], (SHIP_WIDTH, SHIP_HEIGHT))
assets['bullet_img'] = pygame.image.load('assets/img/laserRed16.png').convert_alpha()

# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
boom_sound = pygame.mixer.Sound('assets/snd/expl3.wav')
destroy_sound = pygame.mixer.Sound('assets/snd/expl6.wav')
assets['river_sound'] = pygame.mixer.Sound('assets/snd/pew.wav')
assets['croco_sound'] = pygame.mixer.Sound('assets/snd/expl3.wav')
assets['dj_sound'] =  pygame.mixer.Sound('assets/snd/expl6.wav')