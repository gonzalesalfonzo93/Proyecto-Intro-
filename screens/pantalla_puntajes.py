import pygame
from utilities.gestor_puntajes import obtener_top_puntajes
from utilities.utils import crear_boton

def mostrar_pantalla_puntajes(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 26)

    while True:
        pantalla.fill((20, 20, 50))
        titulo = fuente.render("Mejores Puntajes", True, (255, 255, 0))
        pantalla.blit(titulo, (290, 40))

        top = obtener_top_puntajes()
        for i, (nombre, puntos) in enumerate(top):
            texto = fuente.render(f"{i+1}. {nombre} - {puntos}", True, (255, 255, 255))
            pantalla.blit(texto, (250, 100 + i * 40))

        if crear_boton(pantalla, "Volver", (300, 400), None):
            return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        reloj.tick(60)
