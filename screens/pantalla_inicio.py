import pygame
import sys
from screens.pantalla_personalizacion import mostrar_pantalla_personalizacion
from screens.pantalla_configuracion import mostrar_pantalla_configuracion
from screens.pantalla_puntajes import mostrar_pantalla_puntajes
from screens.pantalla_informacion import mostrar_pantalla_informacion
from utilities.utils import crear_boton

def mostrar_pantalla_inicio(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arcade", 40)
    fondo_color = (30, 30, 30)

    while True:
        pantalla.fill(fondo_color)

        titulo = fuente.render("BOMBERMAN RETRO", True, (255, 255, 255))
        pantalla.blit(titulo, (pantalla.get_width() // 2 - titulo.get_width() // 2, 100))

        # Lista de botones con acciones usando lambda para pasar pantalla
        botones = [
            ("Iniciar Juego", lambda: mostrar_pantalla_personalizacion(pantalla)),
            ("Configuración", lambda: mostrar_pantalla_configuracion(pantalla)),
            ("Mejores Puntajes", lambda: mostrar_pantalla_puntajes(pantalla)),
            ("Información", lambda: mostrar_pantalla_informacion(pantalla)),
            ("Salir", sys.exit),
        ]

        for i, (texto, accion) in enumerate(botones):
            if crear_boton(pantalla, texto, (300, 220 + i * 70), accion):
                return  # Salta al siguiente menú

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.flip()
        reloj.tick(60)
