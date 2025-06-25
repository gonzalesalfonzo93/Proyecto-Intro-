import pygame
from utilities.musica import ControladorMusica
from utilities.utils import crear_boton

def mostrar_pantalla_configuracion(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arial", 30)
    musica = ControladorMusica()

    while True:
        pantalla.fill((40, 40, 80))
        texto = fuente.render("Configuración", True, (255, 255, 255))
        pantalla.blit(texto, (300, 50))

        estado = "Activada" if musica.activa else "Desactivada"
        if crear_boton(pantalla, f"Música: {estado}", (280, 200), musica.toggle):
            pass

        if crear_boton(pantalla, "Volver", (280, 300), None):
            return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()

        pygame.display.flip()
        reloj.tick(60)
