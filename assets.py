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
    assets[CROCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'crocodilo_jogo_da_velha.jpg')).convert_alpha()
    assets[CROCO_IMG] = pygame.transform.scale(assets[CROCO_IMG], (199, 199))
    assets[PESSOA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'imagem_pessoa1.jpeg')).convert_alpha()
    assets[PESSOA_IMG] = pygame.transform.scale(assets[PESSOA_IMG], (195, 195))
    assets[PESSOA_IMG] = pygame.transform.rotate(assets[PESSOA_IMG],270)
    assets[PLAY_INICIAL_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play_inicial.png')).convert_alpha()
    assets[PLAY_INICIAL_IMG] = pygame.transform.scale(assets[PLAY_INICIAL_IMG], (300, 300))
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play_inicial_mais_clara.png')).convert_alpha()
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.transform.scale(assets[PLAY_INICIAL_SELECIONADA_IMG], (300, 300))
# Carrega os sons do jogo
    #pygame.mixer.music.load(os.path.join(SND_DIR, ''))
    #pygame.mixer.music.set_volume(0.4)
    assets[DJ_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'dj_caionoveli-sound.ogg'))
    assets[RIVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'river-sound.ogg'))
    assets[WIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'win-sound.ogg'))
    assets[CROCO_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crocodile-sound.ogg'))
    return assets