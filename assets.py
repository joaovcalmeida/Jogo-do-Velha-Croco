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
CROCO_VENCEU = 'croco_venceu'
DJ_VENCEU = 'dj_venceu'
DEU_VELHA = 'deu_velha'


def load_assets():
    assets = {}
    assets[BACKGROUND] = pygame.image.load(os.path.join(IMG_DIR,'6206152.jpg')).convert()
    assets[CROCO_IMG] = pygame.image.load(os.path.join(IMG_DIR, 'crocodilo_jogo_da_velha.png')).convert_alpha()
    assets[CROCO_IMG] = pygame.transform.scale(assets[CROCO_IMG], (190, 190))
    assets[PESSOA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'imagem_pessoa1.png')).convert_alpha()
    assets[PESSOA_IMG] = pygame.transform.scale(assets[PESSOA_IMG], (190, 190))
    assets[PLAY_INICIAL_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play_inicial.png')).convert_alpha()
    assets[PLAY_INICIAL_IMG] = pygame.transform.scale(assets[PLAY_INICIAL_IMG], (300, 300))
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.image.load(os.path.join(IMG_DIR,'play_inicial_mais_clara.png')).convert_alpha()
    assets[PLAY_INICIAL_SELECIONADA_IMG] = pygame.transform.scale(assets[PLAY_INICIAL_SELECIONADA_IMG], (300, 300))
    assets[CROCO_VENCEU] = pygame.image.load(os.path.join(IMG_DIR,'croco_venceu.png')).convert_alpha()
    assets[CROCO_VENCEU] = pygame.transform.scale(assets[CROCO_VENCEU], (300, 150))
    assets[CROCO_VENCEU] = pygame.transform.rotate(assets[CROCO_VENCEU], 0)
    assets[DJ_VENCEU] = pygame.image.load(os.path.join(IMG_DIR,'dj_novelli_venceu.png')).convert_alpha()
    assets[DJ_VENCEU] = pygame.transform.scale(assets[DJ_VENCEU], (380, 150))
    assets[DJ_VENCEU] = pygame.transform.rotate(assets[DJ_VENCEU], 0)
    assets[DEU_VELHA] = pygame.image.load(os.path.join(IMG_DIR,'deu-velha.png')).convert_alpha()
    assets[DEU_VELHA] = pygame.transform.scale(assets[DEU_VELHA], (300, 150))
    assets[DEU_VELHA] = pygame.transform.rotate(assets[DEU_VELHA], 0)


# Carrega os sons do jogo
    #pygame.mixer.music.load(os.path.join(SND_DIR, ''))
    #pygame.mixer.music.set_volume(0.4)
    assets[DJ_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'vitoria_dj.ogg'))
    assets[RIVER_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'river-sound.ogg'))
    assets[WIN_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'win-sound.ogg'))
    assets[CROCO_SOUND] = pygame.mixer.Sound(os.path.join(SND_DIR, 'crocodilado.ogg'))
    return assets