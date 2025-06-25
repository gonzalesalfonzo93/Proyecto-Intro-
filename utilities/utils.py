import pygame

def crear_boton(pantalla, texto, posicion, accion=None):
    fuente = pygame.font.SysFont("arial", 28)
    rect = pygame.Rect(posicion[0], posicion[1], 250, 40)
    pygame.draw.rect(pantalla, (70, 70, 70), rect)
    pygame.draw.rect(pantalla, (255, 255, 255), rect, 2)

    texto_render = fuente.render(texto, True, (255, 255, 255))
    pantalla.blit(texto_render, (posicion[0] + 10, posicion[1] + 5))

    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if rect.collidepoint(mouse) and click[0]:
        pygame.time.wait(150)
        if accion:
            accion()
        return True
    return False

def cargar_sprite_escalado(path, tamaño):
    imagen = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(imagen, tamaño)
