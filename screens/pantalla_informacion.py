import pygame
from utilities.utils import crear_boton

def mostrar_pantalla_informacion(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 24)

    datos = [
        "Autor: Tu Nombre",
        "ID: 2023xxxx",
        "Curso: IC-1801 Introducción a la Programación",
        "Instituto Tecnológico de Costa Rica",
        "Profesor: Nombre del profesor",
        "Versión: 1.0",
        "",
        "Controles:",
        "Flechas: Mover",
        "X: Colocar bomba",
        "Z: Usar habilidad",
        "C: Detonar bomba remota (solo personaje 3)",
    ]

    while True:
        pantalla.fill((10, 30, 50))
        for i, linea in enumerate(datos):
            texto = fuente.render(linea, True, (255, 255, 255))
            pantalla.blit(texto, (80, 40 + i * 30))

        if crear_boton(pantalla, "Volver", (300, 500), None):
            return  # ← simplemente vuelve al menú anterior sin importar

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        reloj.tick(60)
