import pygame
from utilities.utils import cargar_sprite_escalado

heart = cargar_sprite_escalado("assets/interfaz/heart.png", (16, 16))
bomb_icon = cargar_sprite_escalado("assets/interfaz/bomb_icon.png", (16, 16))
key_icon = cargar_sprite_escalado("assets/interfaz/key_icon.png", (16, 16))

def dibujar_hud(pantalla, jugador, vidas, puntos, tiempo_inicio):
    fuente = pygame.font.SysFont("arial", 20)
    y = 11 * 32 + 5

    # Vidas
    for i in range(jugador.vida):
        pantalla.blit(heart, (10 + i * 20, y))

    # Bombas
    pantalla.blit(bomb_icon, (200, y))
    pantalla.blit(fuente.render(f"x {jugador.bombas}", True, (255, 255, 255)), (220, y))

    # Llave
    if jugador.llave:
        pantalla.blit(key_icon, (300, y))

    # Puntos
    pantalla.blit(fuente.render(f"Puntos: {puntos}", True, (255, 255, 0)), (400, y))

    # Tiempo
    segundos = (pygame.time.get_ticks() - tiempo_inicio) // 1000
    pantalla.blit(fuente.render(f"Tiempo: {segundos}s", True, (255, 255, 255)), (600, y))
