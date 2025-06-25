import pygame
from screens.pantalla_juego import iniciar_juego
from utilities.utils import crear_boton, cargar_sprite_escalado

def mostrar_pantalla_personalizacion(pantalla):
    reloj = pygame.time.Clock()
    fuente = pygame.font.SysFont("arcade", 28)
    nombre = ""
    skin_seleccionada = 1
    escribiendo = True

    skins = [
        cargar_sprite_escalado("assets/personajes/player1_down_idle.png", (32, 32)),
        cargar_sprite_escalado("assets/personajes/player2_down_idle.png", (32, 32)),
        cargar_sprite_escalado("assets/personajes/player3_down_idle.png", (32, 32)),
    ]

    descripciones = [
        "Vida: 3 | Bombas: 1 | Daño: 1 | Explosión +1",
        "Vida: 2 | Bombas: 2 | Daño: 1 | Dispara bola de fuego",
        "Vida: 3 | Bombas: 1 | Daño: 2 | Bomba remota"
    ]

    while True:
        pantalla.fill((20, 20, 60))

        titulo = fuente.render("Personalización", True, (255, 255, 255))
        pantalla.blit(titulo, (pantalla.get_width() // 2 - titulo.get_width() // 2, 40))

        texto = fuente.render("Nombre:", True, (255, 255, 255))
        pantalla.blit(texto, (200, 120))

        input_nombre = fuente.render(nombre + ("_" if escribiendo else ""), True, (200, 200, 200))
        pantalla.blit(input_nombre, (320, 120))

        pantalla.blit(fuente.render("Selecciona tu personaje:", True, (255, 255, 255)), (200, 200))
        for i, skin in enumerate(skins):
            x = 250 + i * 100
            y = 250
            pantalla.blit(skin, (x, y))
            if i + 1 == skin_seleccionada:
                pygame.draw.rect(pantalla, (255, 255, 0), (x - 5, y - 5, 42, 42), 2)

            desc = fuente.render(descripciones[i], True, (180, 180, 180))
            pantalla.blit(desc, (x - 60, 300))

        if crear_boton(pantalla, "Comenzar", (300, 400), None):
            if nombre.strip() != "":
                iniciar_juego(pantalla, nombre, skin_seleccionada)
                return

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif evento.type == pygame.KEYDOWN:
                if escribiendo:
                    if evento.key == pygame.K_BACKSPACE:
                        nombre = nombre[:-1]
                    elif evento.key == pygame.K_RETURN:
                        escribiendo = False
                    elif len(nombre) < 10:
                        nombre += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                for i in range(3):
                    if 250 + i * 100 <= mx <= 282 + i * 100 and 250 <= my <= 282:
                        skin_seleccionada = i + 1

        pygame.display.flip()
        reloj.tick(60)
