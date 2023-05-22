import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
CROCO_IMG = 'croco_img'
PESSOA_IMG = 'pessoa_img'
PLAY_INICIAL_IMG = 'play_inicial_img'
PLAY_INICIAL_SELECIONADA_IMG = 'play_inicial_selecionada_img'
CROCO_SOUND = 'croco_sound'
DJ_SOUND = 'dj_sound'
RIVER_SOUND ='river_sound'
WIN_SOUND = 'win_sound'





def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,'6206152.jpg')).convert()
    assets[CROCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'crocodilo jogo da velha.png')).convert_alpha()
    assets[PESSOA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'imagem pessoa.png')).convert_alpha()
    assets[PLAY_INICIAL_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play inicial.png')).convert_alpha()
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play inicial mais clara.png')).convert_alpha()

# Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, ''))
    pygame.mixer.music.set_volume(0.4)
    assets[DJ_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl3.wav'))
    assets[RIVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'expl6.wav'))
    assets[WIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'pew.wav'))
    return assets