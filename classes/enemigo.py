import pygame
import random
from utilities.utils import cargar_sprite_escalado

class Enemigo:
    def __init__(self, tipo, x, y, matriz):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.vivo = True
        self.matriz = matriz
        self.direccion = "down"
        self.frame = 0
        self.tiempo_frame = pygame.time.get_ticks()
        self.sprites = self.cargar_animaciones()

    def cargar_animaciones(self):
        base = f"assets/enemigos/enemy{self.tipo}_"
        return {
            "down": [
                cargar_sprite_escalado(base + "down_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "down_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "down_walk_2.png", (32, 32)),
            ],
            "up": [
                cargar_sprite_escalado(base + "up_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "up_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "up_walk_2.png", (32, 32)),
            ],
            "left": [
                cargar_sprite_escalado(base + "left_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "left_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "left_walk_2.png", (32, 32)),
            ],
            "right": [
                cargar_sprite_escalado(base + "right_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "right_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "right_walk_2.png", (32, 32)),
            ],
        }

    def mover(self):
        if not self.vivo:
            return
        direccion = random.choice(["up", "down", "left", "right"])
        dx, dy = 0, 0
        if direccion == "up": dy = -1
        elif direccion == "down": dy = 1
        elif direccion == "left": dx = -1
        elif direccion == "right": dx = 1

        nx, ny = self.x + dx, self.y + dy
        if 0 <= nx < 13 and 0 <= ny < 11 and self.matriz[ny][nx] == " ":
            self.x, self.y = nx, ny
            self.direccion = direccion

        ahora = pygame.time.get_ticks()
        if ahora - self.tiempo_frame > 200:
            self.frame = (self.frame + 1) % 3
            self.tiempo_frame = ahora

    def dibujar(self, pantalla):
        if self.vivo:
            img = self.sprites[self.direccion][self.frame]
            pantalla.blit(img, (self.x * 32, self.y * 32))

class GestorEnemigos:
    def __init__(self, lista_tipos, jefe, matriz):
        self.lista = [Enemigo(t, random.randint(1, 11), random.randint(1, 9), matriz) for t in lista_tipos]
        self.jefe = jefe

    def actualizar(self, jugador):
        for enemigo in self.lista:
            enemigo.mover()
            if enemigo.vivo and enemigo.x == jugador.x and enemigo.y == jugador.y:
                jugador.vida -= 1

    def dibujar(self, pantalla):
        for enemigo in self.lista:
            enemigo.dibujar(pantalla)
