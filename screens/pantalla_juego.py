import pygame
from classes.jugador import Jugador
from classes.bomba import GestorBombas
from classes.item import GestorItems
from classes.enemigo import GestorEnemigos
from features.background import generar_mapa, dibujar_mapa
from features.hud import dibujar_hud
from features.gestor_niveles import cargar_datos_nivel, avanzar_nivel
from utilities.musica import reproducir_musica_nivel
from classes.proyectil import Proyectil

def iniciar_juego(pantalla, nombre, skin_id):
    reloj = pygame.time.Clock()
    nivel_actual = 1
    puntos = 0
    vidas = 3

    while nivel_actual <= 4 and vidas > 0:
        # Preparar nivel
        fondo_color, enemigos, jefe, tipo_nivel = cargar_datos_nivel(nivel_actual)
        matriz = generar_mapa(nivel_actual)
        reproducir_musica_nivel(nivel_actual)

        # Inicializar entidades
        jugador = Jugador(nombre, skin_id, matriz, tipo_nivel)
        bombas = GestorBombas(jugador)
        enemigos_gestor = GestorEnemigos(enemigos, jefe, matriz)
        items = GestorItems()
        proyectiles = []

        tiempo_inicio = pygame.time.get_ticks()
        ejecutando = True

        while ejecutando:
            pantalla.fill(fondo_color)

            # EVENTOS
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    pygame.quit()
                    exit()
                elif evento.type == pygame.KEYDOWN:
                    if evento.key == pygame.K_x:
                        bombas.colocar_bomba(jugador)
                    elif evento.key == pygame.K_z:
                        jugador.activar_habilidad(proyectiles, bombas)
                    elif evento.key == pygame.K_c:
                        jugador.detonar_remota(bombas)

            teclas = pygame.key.get_pressed()
            jugador.mover(teclas)

            # ACTUALIZACIONES
            bombas.actualizar(matriz, enemigos_gestor, jugador, items)
            enemigos_gestor.actualizar(jugador)
            items.actualizar(jugador)

            for proyectil in proyectiles:
                proyectil.mover(matriz)
                proyectil.colisiona(jugador)
            proyectiles = [p for p in proyectiles if p.vivo]

            # DIBUJO
            dibujar_mapa(pantalla, matriz)
            bombas.dibujar(pantalla)
            enemigos_gestor.dibujar(pantalla)
            items.dibujar(pantalla)
            for p in proyectiles:
                p.dibujar(pantalla)
            jugador.dibujar(pantalla)
            dibujar_hud(pantalla, jugador, vidas, puntos, tiempo_inicio)

            # CONDICIONES
            if jugador.vida <= 0:
                vidas -= 1
                ejecutando = False

            if avanzar_nivel(jugador, matriz, nivel_actual):
                puntos += 100
                nivel_actual += 1
                ejecutando = False

            pygame.display.flip()
            reloj.tick(60)

    # Fin del juego
    from screens.pantalla_final import mostrar_pantalla_final
    mostrar_pantalla_final(pantalla, jugador.nombre, puntos, nivel_actual > 4)
