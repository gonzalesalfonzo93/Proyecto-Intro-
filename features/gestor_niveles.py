def cargar_datos_nivel(nivel):
    if nivel == 1:
        return (50, 150, 50), [1], None, "normal"
    elif nivel == 2:
        return (139, 69, 19), [2], None, "normal"
    elif nivel == 3:
        return (180, 240, 255), [3], None, "hielo"  # celeste hielo
    elif nivel == 4:
        return (150, 0, 0), [], "boss", "jefe"
    return (0, 0, 0), [], None, "normal"

def avanzar_nivel(jugador, matriz, nivel_actual):
    if nivel_actual < 4:
        if matriz[jugador.y][jugador.x] == "U" and jugador.llave:
            return True
    else:
        if jugador.llave:  # jefe derrotado
            return True
    return False
