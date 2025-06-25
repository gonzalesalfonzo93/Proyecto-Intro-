import pygame
import random
from utilities.utils import cargar_sprite_escalado

# Carga de sprites
brick_borde = cargar_sprite_escalado("assets/bloques/brick_borde.png", (32, 32))
brick_indestructible = cargar_sprite_escalado("assets/bloques/brick_indestructible.png", (32, 32))
brick_destructible = cargar_sprite_escalado("assets/bloques/brick_destructible.png", (32, 32))
puerta = cargar_sprite_escalado("assets/bloques/door.png", (32, 32))
llave = cargar_sprite_escalado("assets/bloques/key.png", (32, 32))

def generar_mapa(nivel):
    mapa = []
    for y in range(11):
        fila = []
        for x in range(13):
            if x == 0 or x == 12 or y == 0 or y == 10:
                fila.append("B")
            elif x % 2 == 0 and y % 2 == 0:
                fila.append("I")
            elif random.random() < 0.3:
                fila.append("D")
            else:
                fila.append(" ")
        mapa.append(fila)

    for (x, y) in [(1, 1), (1, 2), (2, 1)]:
        mapa[y][x] = " "

    destructibles = [(x, y) for y in range(11) for x in range(13) if mapa[y][x] == "D"]
    random.shuffle(destructibles)
    if len(destructibles) >= 2:
        mapa[destructibles[0][1]][destructibles[0][0]] = "K"
        mapa[destructibles[1][1]][destructibles[1][0]] = "P"

    return mapa

def dibujar_mapa(pantalla, mapa):
    for y, fila in enumerate(mapa):
        for x, celda in enumerate(fila):
            if celda == "B":
                pantalla.blit(brick_borde, (x * 32, y * 32))
            elif celda == "I":
                pantalla.blit(brick_indestructible, (x * 32, y * 32))
            elif celda == "D":
                pantalla.blit(brick_destructible, (x * 32, y * 32))
            elif celda == "K" or celda == "P":
                pantalla.blit(brick_destructible, (x * 32, y * 32))
            elif celda == "L":
                pantalla.blit(llave, (x * 32, y * 32))
            elif celda == "U":
                pantalla.blit(puerta, (x * 32, y * 32))
