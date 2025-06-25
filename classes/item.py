import pygame
from utilities.utils import cargar_sprite_escalado

powerups = {
    "vida": cargar_sprite_escalado("assets/powerups/powerup_life.png", (32, 32)),
    "damage": cargar_sprite_escalado("assets/powerups/powerup_damage.png", (32, 32))
}
items = {
    "congelar": cargar_sprite_escalado("assets/items/item_congelar.png", (32, 32)),
    "invencible": cargar_sprite_escalado("assets/items/item_invencibilidad.png", (32, 32)),
    "pasarmuros": cargar_sprite_escalado("assets/items/item_pasarmuros.png", (32, 32)),
}

class Item:
    def __init__(self, tipo, x, y):
        self.tipo = tipo
        self.x = x
        self.y = y
        self.visible = True

    def aplicar(self, jugador):
        if self.tipo == "vida":
            jugador.vida += 1
        elif self.tipo == "damage":
            pass  # Puedes incrementar daño temporal aquí
        elif self.tipo == "congelar":
            pass  # Puedes implementar congelamiento de enemigos
        elif self.tipo == "invencible":
            pass
        elif self.tipo == "pasarmuros":
            pass
        self.visible = False

    def dibujar(self, pantalla):
        if self.visible:
            img = powerups.get(self.tipo) or items.get(self.tipo)
            pantalla.blit(img, (self.x * 32, self.y * 32))

class GestorItems:
    def __init__(self):
        self.items = []

    def actualizar(self, jugador):
        for item in self.items:
            if item.visible and item.x == jugador.x and item.y == jugador.y:
                item.aplicar(jugador)

    def dibujar(self, pantalla):
        for item in self.items:
            item.dibujar(pantalla)
