import pygame
import os

class ControladorMusica:
    def __init__(self):
        self.activa = True

    def toggle(self):
        self.activa = not self.activa
        if self.activa:
            pygame.mixer.music.unpause()
        else:
            pygame.mixer.music.pause()

def reproducir_musica_nivel(nivel):
    ruta = f"assets/sonidos/nivel{nivel}.mp3"
    if os.path.exists(ruta):
        pygame.mixer.music.load(ruta)
        pygame.mixer.music.play(-1)
