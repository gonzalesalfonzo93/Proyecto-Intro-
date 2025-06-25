import pygame
from utilities.utils import cargar_sprite_escalado

bomb_img = cargar_sprite_escalado("assets/bombas/bomb.png", (32, 32))
explosiones = [
    cargar_sprite_escalado(f"assets/explosiones/explosion_{i}.png", (32, 32))
    for i in range(1, 4)
]

class Bomba:
    def __init__(self, x, y, es_remota=False, rango_extra=False):
        self.x = x
        self.y = y
        self.remota = es_remota
        self.rango_extra = rango_extra
        self.t_explotar = pygame.time.get_ticks() + (999999 if es_remota else 1000)
        self.explotando = False
        self.explotada = False
        self.t_destruir = 0
        self.frame = 0
        self.frame_timer = pygame.time.get_ticks()

    def actualizar(self, matriz, enemigos, jugador, items):
        ahora = pygame.time.get_ticks()
        if not self.explotando and ahora >= self.t_explotar:
            self.explotando = True
            self.t_destruir = ahora + 1000
            self.afectar(matriz, enemigos, jugador)
        elif self.explotando and ahora >= self.t_destruir:
            self.explotada = True

    def afectar(self, matriz, enemigos, jugador):
        alcance = 2 if self.rango_extra else 1
        posiciones = [(self.x, self.y)]
        for dx, dy in [(1,0), (-1,0), (0,1), (0,-1)]:
            for i in range(1, alcance+1):
                nx = self.x + dx*i
                ny = self.y + dy*i
                if 0 <= nx < 13 and 0 <= ny < 11:
                    posiciones.append((nx, ny))
                    if matriz[ny][nx] in ("I", "B"):
                        break

        for x, y in posiciones:
            if matriz[y][x] == "D":
                matriz[y][x] = " "
            elif matriz[y][x] == "K":
                matriz[y][x] = "L"
            elif matriz[y][x] == "P":
                matriz[y][x] = "U"
            if jugador.x == x and jugador.y == y:
                jugador.vida -= 1
            for enemigo in enemigos.lista:
                if enemigo.x == x and enemigo.y == y:
                    enemigo.vivo = False

    def detonar(self):
        self.t_explotar = pygame.time.get_ticks()

    def dibujar(self, pantalla):
        if self.explotando:
            ahora = pygame.time.get_ticks()
            if ahora - self.frame_timer > 100:
                self.frame = (self.frame + 1) % len(explosiones)
                self.frame_timer = ahora
            pantalla.blit(explosiones[self.frame], (self.x * 32, self.y * 32))
        else:
            pantalla.blit(bomb_img, (self.x * 32, self.y * 32))

class GestorBombas:
    def __init__(self, jugador=None):
        self.bombas = []
        self.rango_extra = False
        self.jugador = jugador

    def colocar_bomba(self, jugador):
        if len([b for b in self.bombas if not b.remota]) < jugador.bombas:
            b = Bomba(jugador.x, jugador.y, es_remota=False, rango_extra=self.rango_extra)
            self.bombas.append(b)
            self.rango_extra = False  # reset tras usar
            return b

    def colocar_bomba_remota(self, x, y):
        b = Bomba(x, y, es_remota=True)
        self.bombas.append(b)
        return b

    def detonar_remota(self, bomba):
        if bomba in self.bombas:
            bomba.detonar()

    def actualizar(self, matriz, enemigos, jugador, items):
        for b in self.bombas:
            b.actualizar(matriz, enemigos, jugador, items)
        self.bombas = [b for b in self.bombas if not b.explotada]

    def dibujar(self, pantalla):
        for b in self.bombas:
            b.dibujar(pantalla)
