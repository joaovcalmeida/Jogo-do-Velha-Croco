import pygame
import os
from config import IMG_DIR, SND_DIR, FNT_DIR


BACKGROUND = 'background'
CROCO_IMG = 'croco_img'
PESSOA_IMG = 'pessoa_img'
PLAY_INICIAL_IMG='play_inicial_img'
PLAY_INICIAL_SELECIONADA_IMG = 'play_inicial_selecionada_img'
CROCO_SOUND = 'croco_sound'
DJ_SOUND = 'dj_sound'
RIVER_SOUND ='river_sound'
WIN_SOUND = 'win_sound'

def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,'6206152.jpg')).convert()
    assets[CROCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'crocodilo jogo da velha.jpg')).convert_alpha()
    assets[PESSOA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'imagem pessoa 1,jpeg')).convert_alpha()
    assets[PLAY_INICIAL_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play inicial.png')).convert_alpha()
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play inicial mais clara.png')).convert_alpha()
# Carrega os sons do jogo
    pygame.mixer.music.load(os.path.join(SND_DIR, ''))
    pygame.mixer.music.set_volume(0.4)
    assets[DJ_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'dj_caionoveli sound.m4a'))
    assets[RIVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'river sound.mp3'))
    assets[WIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'win sound.mp3'))
    assets[CROCO_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crocodile sound.mp3'))
    return assets

# Jogo-do-Velha-Croco

# ----- Inicia assets
CROCODILO_WIDTH = 300
CROCODILO_HEIGHT = 300
PLAY_INICIAL_WIDTH = 600
PLAY_INICIAL_HEIGHT = 600
PLAY_SELECIONADA_WIDTH = 600
PLAY_SELECIONADA_HEIGHT =600
PESSOA_WIDTH = 300
PESSOA_HEIGHT = 300
BACKGROUND_WIDTH = 800
BACKGROUND_HEIGHT = 600

assets={}
assets['background'] = pygame.image.load('assets/img/img/6206152.jpg').convert()
assets['background'] = pygame.transform.scale(assets['6206152.jpg'], (BACKGROUND_WIDTH, BACKGROUND_HEIGHT))
assets['crocodilo_img'] = pygame.image.load('assets/img/crocodilo jogo da velha.jpg').convert_alpha()
assets['crocodilo_img'] = pygame.transform.scale(assets['crocodilo jogo da velha.jpg'], (CROCODILO_WIDTH,CROCODILO_HEIGHT))
assets['play_inicial_img'] = pygame.image.load('assets/img/play inicial.png').convert_alpha()
assets['play_inicial_img'] = pygame.transform.scale(assets['play inicial.png'], (PLAY_INICIAL_WIDTH, PLAY_INICIAL_HEIGHT))
assets['play_inicial_selecionada_img'] = pygame.image.load('assets/img/play inicial mais clara.png').convert_alpha()
assets['play_inicial_selecionada_img'] = pygame.transform.scale(assets['play inicial mais clara.png'], (PLAY_SELECIONADA_WIDTH , PLAY_SELECIONADA_HEIGHT))
assets['pessoa_img'] = pygame.image.load('assets/img/imagem_pessoa1.png').convert_alpha()
assets['pessoa_img'] = pygame.transform.scale(assets['imagem_pessoa1.png'], (PESSOA_WIDTH, PESSOA_HEIGHT))


# Carrega os sons do jogo
pygame.mixer.music.load('assets/snd/tgfcoder-FrozenJam-SeamlessLoop.ogg')
pygame.mixer.music.set_volume(0.4)
assets['river_sound'] = pygame.mixer.Sound('assets/snd/river sound.mp3')
assets['croco_sound'] = pygame.mixer.Sound('assets/snd/crocodile sound.mp3')
assets['dj_sound'] =  pygame.mixer.Sound('assets/snd/dj_caionoveli sound.m4a')
assets['win_sound'] =  pygame.mixer.Sound('assets/snd/win sound.mp3')
