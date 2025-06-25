import pygame
from utilities.utils import cargar_sprite_escalado
from classes.proyectil import Proyectil

class Jugador:
    def __init__(self, nombre, skin, matriz, tipo_nivel):
        self.nombre = nombre
        self.skin = skin
        self.matriz = matriz
        self.tipo_nivel = tipo_nivel
        self.x = 1
        self.y = 1
        self.direccion = "down"
        self.frame = 0
        self.tiempo_frame = pygame.time.get_ticks()
        self.tiempo_ultimo_mov = pygame.time.get_ticks()
        self.tiempo_habilidad = 0
        self.vida, self.bombas, self.daño = self.estadisticas_por_skin(skin)
        self.llave = False
        self.remota = None  # bomba remota activa
        self.sprites = self.cargar_animaciones()
        self.resbalando = False
        self.direccion_resbalo = None
        self.tiempo_resbalon = 0

    def estadisticas_por_skin(self, skin):
        if skin == 1:
            return 3, 1, 1
        elif skin == 2:
            return 2, 2, 1
        elif skin == 3:
            return 3, 1, 2

    def cargar_animaciones(self):
        base = f"assets/personajes/player{self.skin}_"
        return {
            "down": [
                cargar_sprite_escalado(base + "down_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "down_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "down_walk_2.png", (32, 32))
            ],
            "up": [
                cargar_sprite_escalado(base + "up_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "up_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "up_walk_2.png", (32, 32))
            ],
            "left": [
                cargar_sprite_escalado(base + "left_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "left_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "left_walk_2.png", (32, 32))
            ],
            "right": [
                cargar_sprite_escalado(base + "right_idle.png", (32, 32)),
                cargar_sprite_escalado(base + "right_walk_1.png", (32, 32)),
                cargar_sprite_escalado(base + "right_walk_2.png", (32, 32))
            ]
        }

    def mover(self, teclas):
        dx, dy = 0, 0
        mov = False
        ahora = pygame.time.get_ticks()

        if teclas[pygame.K_UP]:
            dy = -1
            self.direccion = "up"
            mov = True
        elif teclas[pygame.K_DOWN]:
            dy = 1
            self.direccion = "down"
            mov = True
        elif teclas[pygame.K_LEFT]:
            dx = -1
            self.direccion = "left"
            mov = True
        elif teclas[pygame.K_RIGHT]:
            dx = 1
            self.direccion = "right"
            mov = True

        if mov:
            self.resbalando = False
            self.tiempo_resbalon = ahora
            self.direccion_resbalo = (dx, dy)

        elif self.tipo_nivel == "hielo" and ahora - self.tiempo_resbalon < 1000:
            dx, dy = self.direccion_resbalo
            self.resbalando = True
        else:
            self.resbalando = False

        nx = self.x + dx
        ny = self.y + dy
        if 0 <= nx < 13 and 0 <= ny < 11:
            if self.matriz[ny][nx] in (" ", "K", "L", "U"):
                self.x, self.y = nx, ny

        if ahora - self.tiempo_frame > 200:
            self.frame = (self.frame + 1) % 3
            self.tiempo_frame = ahora

    def dibujar(self, pantalla):
        img = self.sprites[self.direccion][self.frame]
        pantalla.blit(img, (self.x * 32, self.y * 32))

    def activar_habilidad(self, proyectiles, gestor_bombas):
        ahora = pygame.time.get_ticks()
        if ahora - self.tiempo_habilidad < 3000:  # cooldown 3s
            return
        self.tiempo_habilidad = ahora

        if self.skin == 1:
            gestor_bombas.rango_extra = True
        elif self.skin == 2:
            dx, dy = {"up": (0, -1), "down": (0, 1), "left": (-1, 0), "right": (1, 0)}[self.direccion]
            proyectiles.append(Proyectil(self.x + dx, self.y + dy, dx, dy, tipo="bola"))
        elif self.skin == 3:
            if self.remota is None:
                self.remota = gestor_bombas.colocar_bomba_remota(self.x, self.y)

    def detonar_remota(self, gestor_bombas):
        if self.remota:
            gestor_bombas.detonar_remota(self.remota)
            self.remota = None
