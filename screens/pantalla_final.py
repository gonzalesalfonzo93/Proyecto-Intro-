import pygame
from utilities.gestor_puntajes import guardar_puntaje
from utilities.utils import crear_boton

def mostrar_pantalla_final(pantalla, nombre, puntos, victoria):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 30)

    guardar_puntaje(nombre, puntos)

    while True:
        pantalla.fill((0, 0, 0))
        resultado = "¡GANASTE!" if victoria else "Has Perdido"
        pantalla.blit(fuente.render(resultado, True, (255, 255, 0)), (320, 100))
        pantalla.blit(fuente.render(f"Puntaje: {puntos}", True, (255, 255, 255)), (320, 160))

        if crear_boton(pantalla, "Volver al menú", (300, 300), None):
            return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        reloj.tick(60)
