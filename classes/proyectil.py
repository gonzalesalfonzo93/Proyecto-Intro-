import pygame
from utilities.utils import cargar_sprite_escalado

bola_img = cargar_sprite_escalado("assets/enemigos/bola_de_fuego.png", (32, 32))

class Proyectil:
    def __init__(self, x, y, dx, dy, tipo="bola"):
        self.x = x
        self.y = y
        self.dx = dx
        self.dy = dy
        self.tipo = tipo
        self.vivo = True
        self.img = bola_img

    def mover(self, matriz):
        self.x += self.dx
        self.y += self.dy
        if not (0 <= self.x < 13 and 0 <= self.y < 11):
            self.vivo = False
        elif matriz[self.y][self.x] in ("I", "D", "B"):
            self.vivo = False

    def colisiona(self, jugador):
        if self.x == jugador.x and self.y == jugador.y:
            jugador.vida -= 1
            self.vivo = False

    def dibujar(self, pantalla):
        pantalla.blit(self.img, (self.x * 32, self.y * 32))
