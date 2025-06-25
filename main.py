import pygame
import sys

# 1. Inicializa Pygame y la pantalla antes que nada
pygame.init()
pantalla = pygame.display.set_mode((832, 704))  # 17x17 grid + HUD
pygame.display.set_caption("Bomberman Retro")

# 2. SOLO AHORA importa módulos que cargan imágenes
from screens import pantalla_inicio
import pygame.mixer
pygame.mixer.init()
pygame.mixer.music.load("assets/sonidos/menu.mp3")
pygame.mixer.music.play(-1)

# 3. Control del flujo del juego
def main():
    siguiente_pantalla = "inicio"

    while True:
        if siguiente_pantalla == "inicio":
            siguiente_pantalla = pantalla_inicio.mostrar_pantalla_inicio(pantalla)
        elif siguiente_pantalla == "salir":
            pygame.quit()
            sys.exit()

if __name__ == "__main__":
    main()
